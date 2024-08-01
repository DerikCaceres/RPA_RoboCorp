import re

def verify_money_in_text(title, description):
    """
    Verifies if there is any mention of money in the given title or description.
    
    Args:
        title (str): The title to check.
        description (str): The description to check.
    
    Returns:
        bool: True if any money-related pattern is found, False otherwise.
    """
    if not title or not description:
        return False

    # Regex patterns for different dollar amount formats
    patterns = [
        r'\$\d+(?:,\d{3})*(?:\.\d{2})?',  # $123,456.78 or $123456.78
        r'US\$\d+(?:,\d{3})*(?:\.\d{2})?', # US$123,456.78 or US$123456.78
        r'\d+(?:,\d{3})*\s+dollars'        # 123,456 dollars or 123456 dollars
    ]

    # Checks if any of the patterns are present in the title or description
    for pattern in patterns:
        if re.search(pattern, title) or re.search(pattern, description):
            return True
    return False

def count_occurrences(title, description, search_phrase):
    """
    Counts the occurrences of the search_phrase in the title and description.
    
    Args:
        title (str): The title to search in.
        description (str): The description to search in.
        search_phrase (str): The phrase to search for.
    
    Returns:
        int: The total number of occurrences of the search_phrase.
    """
    if not title or not description or not search_phrase:
        return 0

    # Convert everything to lowercase to make a case insensitive search
    phrase_searched = search_phrase.lower()

    # Count occurrences in title and description
    occurrences_title = title.lower().count(phrase_searched)
    occurrences_description = description.lower().count(phrase_searched)

    return occurrences_title + occurrences_description

def remove_non_letters(text):
    """
    Removes non-letter characters from the text.
    
    Args:
        text (str): The text to process.
    
    Returns:
        str: The text with non-letter characters removed.
    """
    if not text:
        return ''

    # Use regular expression to replace non-alphabetic characters with an empty string
    return re.sub(r'[^a-zA-Z]', '', text)
