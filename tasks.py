from robocorp.tasks import task
from robocorp import workitems
from p002_yahoo_news import P002_Access_Site
from p003_write_in_excel_file import P003_Write_In_Excel_File
import locale
import sys
import logging

from Assets.Libraries.file import Clear_Images_Folder
from Assets.Libraries.cfg import Settings
import logging



@task
def t01_project_setup():
    """Configurações do projeto"""
    logging.info("Starting the bot...")
    
    locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')  # Corrige o código para 'pt_PT.UTF-8'
    
    try:
        sys.stdout.reconfigure(encoding='utf-8')  # Configura a saída no console com codificação UTF8
    except Exception as e:
        print(f"Erro ao configurar sys.stdout: {e}")

    Clear_Images_Folder(Settings.images_path)

    logging.info("Arquivo Excel criado com sucesso.")
    
@task
def t02_project_process():
    # Access the current input work item
    item = workitems.inputs.current
    print("Received payload:", item.payload)
    
    # Extracting 'search_phrase' and 'date_range' from the payload
    search_phrase = item.payload.get("search_phrase")
    date_range = item.payload.get("date_range")

    # Obtém os dados das notícias
    news_scraper = P002_Access_Site(search_phrase, date_range)
    news_data = news_scraper()
    
    return news_data  # Return the news_data after scraping

@task
def t03_create_excel(news_data):
    # Escreve no arquivo Excel
    P003_Write_In_Excel_File(news_data=news_data)

    logging.info("Bot execution completed.")