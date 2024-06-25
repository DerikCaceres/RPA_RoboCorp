from Assets.Libraries.Data.pandas import DataFramePrettier
from Assets.Libraries.file import CreateFile
from Assets.Libraries.cfg import Settings
import pandas as pd
import logging
import shutil

class P003_Write_In_Excel_File:
    """Registra as informações das notícias em um arquivo Excel"""

    def __init__(self, news_data):
        logging.info("Escrevendo dados no arquivo Excel...")
        self.news_data = news_data
        self.T01_Create_Excel_File()

    def T01_Create_Excel_File(self):
        """Cria um arquivo Excel com as informações das notícias"""

        news_df = pd.DataFrame(self.news_data)

        # Caminho completo para o arquivo Excel de saída
        excel_file_path = Settings.worksheet_news_path

        # DataFrame para Excel
        news_df.to_excel(excel_file_path, index=False)

        # Salva o log
        CreateFile(Settings.log_worksheet, DataFramePrettier(news_df))

        logging.info(f"Arquivo Excel criado com sucesso em: {excel_file_path}")

