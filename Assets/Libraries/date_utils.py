from datetime import datetime

def obtain_months(parameter):
    """
    Obtains a list of full and abbreviated month names for the current month and previous months.
    
    Args:
        parameter (int): The number of previous months to include.
    
    Returns:
        list: A list of month names.
    """
    full_months = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    abbr_months = ["Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.",
                   "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

    current_month = datetime.now().month
    english_months = []

    # Add the current month to the list of English months
    english_months.append(full_months[current_month - 1])
    english_months.append(abbr_months[current_month - 1])

    # Add previous months according to the parameter received
    for i in range(1, parameter):
        last_month = (current_month - 1 - i) % 12
        english_months.append(full_months[last_month])
        english_months.append(abbr_months[last_month])

    return english_months
