from datetime import datetime
import locale
import re

from calendar import month_name, month_abbr
from Assets.Libraries.cfg import Settings


def Verify_money_in_text(title, description):
    # Padrões de regex para diferentes formatos de quantia em dinheiro
    padrao1 = r'\$[\d,.]+'
    padrao2 = r'US\$[\d,.]+'
    padrao3 = r'\d+ dólares'
    padrao4 = r'\d+ dólares'

    # Verifica se algum dos padrões está presente no título ou na descrição
    if re.search(padrao1, title) or re.search(padrao2, title) or re.search(padrao3, title) or re.search(padrao4, title):
        return True
    if re.search(padrao1, description) or re.search(padrao2, description) or re.search(padrao3, description) or re.search(padrao4, description):
        return True

    return False


def Count_ocurrences(title, description):

    # Converter tudo para minúsculas para fazer uma busca case insensitive
    title_lower = title.lower()
    description_lower = description.lower()
    phrase_searched = Settings.search_phrase.lower()
    # Contar ocorrências no título e na descrição
    ocurrences_title = title_lower.count(phrase_searched)
    ocurrences_description = description_lower.count(phrase_searched)


    return ocurrences_title + ocurrences_description


def Obtain_months(parametro):

    full_months = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    abbr_months = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.",
                   "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

    mes_atual = datetime.now().month
    meses_ingleses = []

    # Adicionar o mês atual à lista de meses ingleses
    meses_ingleses.append(full_months[mes_atual - 1])
    meses_ingleses.append(abbr_months[mes_atual - 1])

    # Adicionar meses anteriores conforme o parâmetro recebido
    for i in range(1, parametro):
        mes_anterior = (mes_atual - 1 - i) % 12
        meses_ingleses.append(full_months[mes_anterior])
        meses_ingleses.append(abbr_months[mes_anterior])

    # Retornar a lista de meses
    return meses_ingleses
    
def Remove_Non_Letters(text):
    # Usar expressão regular para substituir caracteres não alfabéticos por uma string vazia
    return re.sub(r'[^a-zA-Z]', '', text)
