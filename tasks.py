from robocorp.tasks import task
from robocorp import workitems
from get_news import Get_News
from write_in_excel_file import Write_In_Excel_File

import sys
import logging

from Assets.Libraries.file import Clear_Images_Folder
from Assets.Libraries.cfg import Settings
import logging



@task
def project_setup():
    """Configures the project for UTF 8 output"""
    logging.info("Starting the bot...")
    
    try:
        sys.stdout.reconfigure(encoding='utf-8') 
    except Exception as e:
        print(f"Erro ao configurar sys.stdout: {e}")

    Clear_Images_Folder(Settings.images_path)

    
@task
def project_process():
    # Access the current input work item
    try:
        item = workitems.inputs.current
        print("Received payload:", item.payload)
        
        # Extracting 'search_phrase' and 'date_range' from the payload
        search_phrase = item.payload.get("search_phrase")
        date_range = item.payload.get("date_range")
    except:
        search_phrase = Settings.search_phrase
        date_range = Settings.date_range

    news_scraper = Get_News(search_phrase, date_range)
    news_data = news_scraper()  # Call the __call__ method to fetch news data

    # Write Excel File
    Write_In_Excel_File(news_data=news_data)

    logging.info("Bot execution completed.")

