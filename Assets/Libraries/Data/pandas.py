
import pandas as pd

def DataFramePrettier(df: pd.DataFrame, tablefmt = 'grid', index = None):
    """ Transforma o DataFrame em uma tabela melhor visível """
    return df.to_markdown(headers='keys', tablefmt=tablefmt, index=index)


