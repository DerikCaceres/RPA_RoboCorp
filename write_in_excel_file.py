import os
import pandas as pd
import logging

class Write_In_Excel_File:
    """Records news information in an Excel file"""

    def __init__(self, news_content):
        logging.info("Writing data Excel...")
        self.news_content = news_content
        self.Create_Excel_File()

    def Create_Excel_File(self):
        """Create an Excel file with news information"""

        news_df = pd.DataFrame(self.news_content)

        excel_file_path = os.path.join('output', 'data_output.xlsx')

        # DataFrame to Excel
        news_df.to_excel(excel_file_path, index=False)


        logging.info(f"Excel file created: {excel_file_path}")

