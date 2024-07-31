import os
import requests
from selenium.webdriver.common.by import By
from Assets.Libraries.text_utils import (
    remove_non_letters,
    verify_money_in_text,
    count_occurrences
)


def get_news_attributes(news, news_parts, news_data, temp_dir, search_phrase):
    """Get the necessary information to put in Excel."""
    
    title = news_parts[1]
    description = news_parts[2]
    
    try:
        page_identifier = ' '.join(title.split(' ')[3:6])
    except IndexError:
        page_identifier = ' '.join(title.split(' ')[0:3])
    
    download_news_image(news, page_identifier, temp_dir)
    
    word_in_text = verify_money_in_text(title, description)
    occurrences = count_occurrences(title, description, search_phrase)

    image_path_in_zip = os.path.join("output", "Images.zip", f"{remove_non_letters(page_identifier)}.png")

    news_data.append({
        "Title": title,
        "Description": description,
        "Image_path": image_path_in_zip,
        "Word_in_text": word_in_text,
        "Occurrences": occurrences
    })

    return news_data


def download_news_image(news, page_identifier, temp_dir):
    """Download the image of each news item and add it to a temporary directory."""
    
    try:
        img_element = news.find_element(By.TAG_NAME, 'img')
        img_url = img_element.get_attribute('src')

        # Download image
        response = requests.get(img_url, stream=True)
        response.raise_for_status()  # Ensure we raise an error for bad HTTP status codes

        # Verify if path exists
        os.makedirs(temp_dir, exist_ok=True)

        filepath = os.path.join(temp_dir, f"{remove_non_letters(page_identifier)}.png")

        # Save image
        with open(filepath, 'wb') as f:
            f.write(response.content)

    except requests.RequestException as e:
        raise Exception(f"Error downloading image: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")
