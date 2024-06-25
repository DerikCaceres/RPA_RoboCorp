from datetime import datetime
import re
from Assets.Libraries.cfg import Settings


def Verify_money_in_text(title, description):
    # Regex patterns for different dollar amount formats
    pattern1 = r'\$[\d,.]+'
    pattern2 = r'US\$[\d,.]+'
    pattern3 = r'\d+ dollars'
    pattern4 = r'\d+ dollars'

    # Checks if any of the patterns are present in the title or description
    if re.search(pattern1, title) or re.search(pattern2, title) or re.search(pattern3, title) or re.search(pattern4, title):
        return True
    if re.search(pattern1, description) or re.search(pattern2, description) or re.search(pattern3, description) or re.search(pattern4, description):
        return True

    return False


def Count_ocurrences(title, description):

    # Convert everything to lowercase to make a case insensitive search
    title_lower = title.lower()
    description_lower = description.lower()
    phrase_searched = Settings.search_phrase.lower()
    # Count occurrences in title and description
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

    # Add the current month to the list of English months
    meses_ingleses.append(full_months[mes_atual - 1])
    meses_ingleses.append(abbr_months[mes_atual - 1])

    # Add previous months according to the parameter received
    for i in range(1, parametro):
        mes_anterior = (mes_atual - 1 - i) % 12
        meses_ingleses.append(full_months[mes_anterior])
        meses_ingleses.append(abbr_months[mes_anterior])

    return meses_ingleses
    
def Remove_Non_Letters(text):
    # Use regular expression to replace non-alphabetic characters with an empty string
    return re.sub(r'[^a-zA-Z]', '', text)
