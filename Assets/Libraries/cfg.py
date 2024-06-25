

class Settings():

    Site_Url = 'https://www.latimes.com/'
    search_phrase = 'economy'
    date_range = 2
    images_path = "Assets\\Libraries\\Images"
    worksheet_news_path = "output\\news.xlsx"
    web_elements = {
        "search":"xpath://button[@data-element='search-button']",
        "search_bar":"xpath://input[@data-element='search-form-input']",
        "confirm_search":"/html/body/div[2]/ps-search-results-module/form",
        "news":"xpath://*/ul[@class='search-results-module-results-menu']/li",

    }
