from robocorp.tasks import task
from robocorp import workitems
from get_news import Get_News
from write_in_excel_file import Write_In_Excel_File
import sys
import logging
from Assets.Libraries.cfg import Settings
import logging

  
@task
def project_process():
        
    logging.info("Starting the bot...")
    
    try:
        sys.stdout.reconfigure(encoding='utf-8') 
    except Exception as e:
        raise Exception (f"Fail to config sys.stdout: {e}")
    
    # Access the current input work item
    try:
        item = workitems.inputs.current
        
        # Extracting 'search_phrase' and 'date_range' from the payload
        search_phrase = item.payload.get("search_phrase")
        date_range = item.payload.get("date_range")
    except:
        search_phrase = Settings.search_phrase
        date_range = Settings.date_range

    news_data = Get_News(search_phrase, date_range)
    news_content = news_data()  # Call the __call__ method to fetch news data

    # Write Excel File
    Write_In_Excel_File(news_content=news_content)

    logging.info("Bot execution completed.")

