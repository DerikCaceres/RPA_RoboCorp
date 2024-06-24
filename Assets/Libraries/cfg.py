from datetime import datetime
import os


       
class Global():
    
    begin_time = datetime.now()
    
    log_directory = begin_time.strftime('./History/%Y/%m/%d/%Y-%m-%d %Hh%Mm%Ss')
    
    errors = list()


class Settings():

    Site_Url = 'https://www.latimes.com/'
    search_phrase = 'economy'
    date_range = 2
    images_path = "Assets\\Libraries\\Images"
    worksheet_news_path = "Assets\\Libraries\\Worksheets\\news.xlsx"
    log_worksheet = os.path.join(Global.log_directory, "Final_worksheet\\Woksheet.log")
    web_elements = {
        "search":"xpath://button[@data-element='search-button']",
        "search_bar":"xpath://input[@data-element='search-form-input']",
        "confirm_search":"/html/body/div[2]/ps-search-results-module/form",
        "news":"xpath://*/ul[@class='search-results-module-results-menu']/li",

    }
