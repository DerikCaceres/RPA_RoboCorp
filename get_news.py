from datetime import time
import os
import tempfile
import logging
import time

from RPA.Browser.Selenium import Selenium
from Assets.Libraries.date_utils import obtain_months
from Assets.Libraries.file import Zip_Images
from Assets.Libraries.get_news_info import get_news_attributes
from Assets.Libraries.cfg import Settings


class GetNews:
    """Open the portal, search for the news, and get the information for each one."""

    def __init__(self, phrase_to_search=None, news_period=None, limit_pages=None):
        logging.info("Accessing the website for information...")
        self.browser = Selenium()
        self.news_data = None
        self.phrase_to_search = phrase_to_search
        self.news_period = news_period
        self.limit_pages = limit_pages

    def __call__(self):
        logging.info("Starting news retrieval process")
        self.open_browser_with_retry()
        self.search_news_with_retry()
        self.news_data = self.get_news_info()
        logging.info("News retrieval process completed")
        return self.news_data
    
    def open_browser_with_retry(self, retries=3):
        """Open the browser and navigate to the website with retry logic."""
        attempt = 0
        while attempt < retries:
            try:
                self.open_browser()
                logging.info("Browser opened successfully")
                return
            except Exception as e:
                attempt += 1
                logging.error(f"Attempt {attempt}: Failed to open browser: {e}")
                if attempt >= retries:
                    raise Exception("Max retries reached for opening browser")
                
    def search_news_with_retry(self, retries=3):
        """Search for news on the portal with retry logic."""
        attempt = 0
        while attempt < retries:
            try:
                self.search_news()
                return
            except Exception as e:
                attempt += 1
                logging.error(f"Attempt {attempt}: Error when searching for news: {e}")
                if attempt >= retries:
                    raise Exception("Max retries reached for searching news")
                

    def open_browser(self):
        """Open the browser and navigate to the website."""
        try:
            self.browser.open_available_browser(Settings.Site_Url, maximized=True)
        except Exception as e:
            raise Exception(f"Failed to open browser: {e}")

        logging.info("Browser opened")


    def search_news(self):
        """Search for news on the portal."""
        try:
            self.browser.wait_until_page_contains_element(Settings.web_elements['search'], timeout=25)
            self.browser.click_element(Settings.web_elements['search'])

            search_input = self.browser.get_webelement(Settings.web_elements['search_bar'])
            self.browser.input_text(search_input, self.phrase_to_search)
            self.browser.press_keys(search_input, 'ENTER')

            self.browser.wait_until_page_contains_element(Settings.web_elements['menu_newest'])

            # Select 'Newest' news
            self.browser.click_element(Settings.web_elements['newest'])
            select_input = self.browser.get_webelement(Settings.web_elements['newest'])
            self.browser.wait_until_page_contains_element(Settings.web_elements['menu_newest'])
            self.browser.select_from_list_by_label(select_input, 'Newest')
            logging.info("Selected 'Newest' news")

        except Exception as e:
            raise Exception(f"Error when searching for news: {e}")

        logging.info("News obtained")

    def get_news_info(self):
        """Get information from the news found."""
        all_news_obtained = False
        news_data = []
        months_possible = obtain_months(self.news_period)
        logging.info(f"Months considered: {months_possible}")

        time.sleep(5)
        count = 0
        with tempfile.TemporaryDirectory() as temp_dir:
            while not all_news_obtained:
                self.browser.wait_until_page_contains_element(Settings.web_elements['news'], timeout=25)
                news_elements = self.browser.find_elements(Settings.web_elements['news'])
                logging.info(f"Found {len(news_elements)} news elements on page {count + 1}")

                if not news_elements:
                    all_news_obtained = True
                    logging.info("No news elements found, stopping search")
                    break

                
                for news in news_elements:

                    news_content = news.text.split('\n')
                    if news_content[1] == 'FOR SUBSCRIBERS':
                        news_content.pop(1)
                    try:
                        date = news_content[3]
                    except:
                        date = news_content[2]

                    if (any(month in date for month in months_possible) or
                        'hours ago' in date or
                        'minutes ago' in date or
                        'hour ago' in date):

                        news_data = get_news_attributes(
                            news,
                            news_content,
                            news_data,
                            temp_dir,
                            self.phrase_to_search
                        )
                    else:
                        break
                    
                if not all_news_obtained:
                    try:
                        count+=1
                        self.browser.click_element('class=search-results-module-next-page')
                    except Exception:
                        break


                if count >= self.limit_pages:

                    logging.info(f"Reached limit of {self.limit_pages} pages, stopping search")
                    break
                    
            output_zip = os.path.join('output', 'news_images.zip')
            Zip_Images(temp_dir, output_zip)

        return news_data
