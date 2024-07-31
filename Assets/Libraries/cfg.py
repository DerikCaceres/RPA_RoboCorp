

class Settings():

    Site_Url = 'https://www.latimes.com/'
    search_phrase = 'economy'
    date_range = 2
    worksheet_news_path = "output\\news.xlsx"
    web_elements = {
        "search":"css:button[data-element='search-button']",
        "search_bar":"css:input[data-element='search-form-input']",
        "news":"css:ul.search-results-module-results-menu > li",
        "sort by":"select-label"
    }
