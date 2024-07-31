
import os
import tempfile
from RPA.Browser.Selenium import Selenium

import time
from Assets.Libraries.date_utils import obtain_months
from Assets.Libraries.file import Zip_Images
from Assets.Libraries.get_news_info import Get_News_Atributtes
from Assets.Libraries.cfg import Settings
import logging

class Get_News:
    """Open the portal, search for the news and get the information for each one"""
    
    def __init__(self, search_phrase=None, date_range=None):
        logging.info("Accessing the website for information...")
        self.browser = Selenium()
        self.news_data = None
        self.search_phrase = search_phrase
        self.date_range = date_range
    
    def __call__(self):
        self.Open_Browser()
        self.Search_News()
        self.news_data = self.Get_NewsInfo()
        return self.news_data


    def Open_Browser(self): 
        try:
            # Abrir o navegador
            self.browser.open_available_browser(Settings.Site_Url, maximized=True)
        except Exception as e:
            raise Exception(f"Failed to open browser: {e}")
        
        logging.info("Browser openned")


    def Search_News(self):
        """Search for news on the portal"""
        
        try:
            # Wait until the search element is available on the page
            self.browser.wait_until_page_contains_element(Settings.web_elements['search'], timeout=25)
            self.browser.click_element(Settings.web_elements['search'])

            # Write on search bar
            search_input = self.browser.get_webelement(Settings.web_elements['search_bar'])
            self.browser.input_text(search_input, self.search_phrase)
            # Press enter 
            self.browser.press_keys(search_input, 'ENTER')
            self.browser.wait_until_page_contains_element('class=select-label')
            #Selecet newest news
            self.browser.click_element('class=select-input')
            select_input = self.browser.get_webelement('class=select-input')
            self.browser.wait_until_page_contains_element('class=select-label')
            self.browser.select_from_list_by_label(select_input, 'Newest')
            
            
        
        except Exception as e:
            raise Exception(f"Error when searching for news: {e}")
        
        logging.info("News obtained")


    def Get_NewsInfo(self):
        """Get information from the news found"""


        all_news_obtained = False
        news_data = []
        #Get valid search months
        months = obtain_months(self.date_range)

        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            while not all_news_obtained:

                self.browser.wait_until_page_contains_element(Settings.web_elements['news'], timeout=25)
                news_elements = self.browser.find_elements(Settings.web_elements['news'])

                if not news_elements:
                    # If there are no more news elements, exit the loop
                    all_news_obtained = True
                    break

                for news in news_elements:
                    news_parts = news.text.split('\n')
                    if news_parts[1] == 'FOR SUBSCRIBERS':
                        news_parts.pop(1)
                    date = news_parts[3]
                    if any(month in date for month in months) or 'hours ago' in date or 'minutes ago' in date or 'hour ago' in date:
                        news_data = Get_News_Atributtes(news, news_parts, news_data, temp_dir, self.search_phrase)


                if not all_news_obtained:
                    #Advance to the next page
                    try:
                        self.browser.click_element('class=search-results-module-next-page')
                    except:
                        all_news_obtained = True
                        pass


            # After downloading all images, create a zip file
            output_zip = os.path.join('output', 'news_images.zip')
            Zip_Images(temp_dir, output_zip)

        return news_data
