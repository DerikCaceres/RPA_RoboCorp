    
import os
import requests
from selenium.webdriver.common.by import By
from Assets.Libraries.Data.data import Count_ocurrences, Remove_Non_Letters, Verify_money_in_text


def Get_News_Atributtes(news, news_parts, news_data, temp_dir):
    """Get the necessary information to put in Excel"""

    title = news_parts[1]
    description = news_parts[2]
    
    try:
        page_identifier = ' '.join(title.split(' ')[3:6])
    except:
        page_identifier = ' '.join(title.split(' ')[0:3])
    #getting image
    
    Download_news_Image(news, page_identifier, temp_dir)
    word_in_text = Verify_money_in_text(title, description)
    ocurrences = Count_ocurrences(title, description)


    image_path_in_zip = os.path.join("output", "Images.zip", f"{page_identifier}.png")


    news_data.append({
        "Title": title,
        "Description": description,
        "Image_path": image_path_in_zip,
        "Word_in_text": word_in_text,
        "Occurrences": ocurrences
    })

    return news_data


def Download_news_Image(news, page_identifier, temp_dir):
    """Download the image of each news item and add a temporary directory to be delivered to the output at the end of execution"""
    try:
        img_element = news.find_element(By.TAG_NAME, 'img')
        img_url = img_element.get_attribute('src')

        # Download image
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            # Verify if path exists
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            filepath = os.path.join(temp_dir, f"{Remove_Non_Letters(page_identifier)}.png")

            # Save image
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Image saved to {filepath}")
        else:
            print(f"Unable to download image. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading image: {str(e)}")