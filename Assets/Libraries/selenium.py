    
import os

import requests
from selenium.webdriver.common.by import By
from Assets.Libraries.Data.data import Count_ocurrences, Remove_Non_Letters, Verify_money_in_text
from Assets.Libraries.cfg import Settings



def Get_News_Atributtes(news, news_parts, news_data):
    """Get the necessary information to put in Excel"""

    title = news_parts[1]  
    description = news_parts[2]
    
    try:
        page_identifier = ' '.join(title.split(' ')[3:6])
    except:
        page_identifier = ' '.join(title.split(' ')[0:3])
    #getting image
    filepath = Download_news_Image(news, page_identifier)
    word_in_text = Verify_money_in_text(title, description)
    ocurrences = Count_ocurrences(title, description)

    news_data.append({
        "Title": title,
        "Description": description,
        "Filepath": filepath,
        "Word_in_text": word_in_text,
        "Occurrences": ocurrences
    })

    return news_data


def Download_news_Image(news, page_identifier):
    try:
        img_element = news.find_element(By.TAG_NAME, 'img')
        img_url = img_element.get_attribute('src')

        # Download image
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            # Verify if path exists
            if not os.path.exists(Settings.images_path):
                os.makedirs(Settings.images_path)

           
            filepath = os.path.join(Settings.images_path, f"{Remove_Non_Letters(page_identifier)}.png")

            # Save image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            return filepath
    
        else:
            print(f"Não foi possível baixar a imagem. Código de status: {response.status_code}")

    except Exception as e:
        print(f"Erro ao baixar a imagem: {str(e)}")