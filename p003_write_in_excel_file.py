from Assets.Libraries.Data.pandas import DataFramePrettier
from Assets.Libraries.file import CreateFile
from Assets.Libraries.cfg import Settings
import pandas as pd
import logging

class P003_Write_In_Excel_File:
    """Registra as informações das notícias em um arquivo Excel"""
    
    def __init__(self, news_data):
        logging.info("Escrevendo dados no arquivo Excel...")
        self.news_data = news_data
        self.T01_Create_Excel_File()

    def T01_Create_Excel_File(self):
        """Cria um arquivo Excel com as informações das notícias"""

        news_df = pd.DataFrame(self.news_data)

        # DataFrame para Excel
        news_df.to_excel(Settings.worksheet_news_path, index=False)

        # Salva o log
        CreateFile(Settings.log_worksheet, DataFramePrettier(news_df))

        logging.info("Arquivo Excel criado com sucesso.")
