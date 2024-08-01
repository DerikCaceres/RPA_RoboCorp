import sys
import logging

from robocorp.tasks import task
from robocorp import workitems

from get_news import GetNews
from write_in_excel_file import Write_In_Excel_File
from Assets.Libraries.cfg import Settings


@task
def project_process():
    """Main function to fetch news and write to an Excel file."""
    
    logging.info("Starting the bot...")

    # Configure stdout to handle UTF-8
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception as e:
        raise Exception(f"Failed to configure sys.stdout: {e}")
    
    try:
        item = workitems.inputs.current
        search_phrase = item.payload.get("search_phrase")
        date_range = item.payload.get("date_range")
        limit_pages = item.payload.get("limit_pages")
    except:
        search_phrase = Settings.search_phrase
        date_range = Settings.date_range
        limit_pages = Settings.limit_pages

    # Instantiate Get_News and fetch news content
    news_scraper = GetNews(search_phrase, date_range, limit_pages)
    news_content = news_scraper()  # Call the __call__ method to fetch news data

    # Write news content to Excel file
    Write_In_Excel_File(news_content=news_content)

    logging.info("Bot execution completed.")
