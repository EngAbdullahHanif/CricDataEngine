# data_processing.py
import pandas as pd
import re

# --------- Data Processing Functions --------- #

def process_cricbuzz_data(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'MatchName': item.get('MatchName', 'N/A'),
            'Venue': item.get('Venue', 'N/A'),
            'Result': item.get('Result', 'N/A')
        }
        processed_data.append(processed_item)
    return processed_data

def process_cricket_news_info(data):
    # Handling missing values, converting data types, and text processing
    processed_data = []
    for item in data:
        processed_item = {
            'Headline': item.get('Headline', 'N/A'),
            'Content': item.get('Content', 'N/A'),
            'Author': item.get('Author', 'Unknown'),
            'PublicationDate': pd.to_datetime(item.get('PublicationDate', 'N/A'), errors='coerce').strftime('%Y-%m-%d')
        }
        processed_data.append(processed_item)
    return processed_data

def process_team_stats(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'Position': item.get('Position', 'N/A'),
            'Name': item.get('Name', 'N/A'),
            'Rating': item.get('Rating', 'N/A'),
            'Points': item.get('Points', 'N/A'),
            'Game': item.get('Game', 'N/A'),
        }
        processed_data.append(processed_item)
    return processed_data

def process_player_stats(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'Position': item.get('Position', 'N/A'),
            'Name': item.get('Name', 'N/A'),
            'Country': item.get('Country', 'N/A'),
            'Rating': item.get('Rating', 'N/A'),
            'Game': item.get('Game', 'N/A'),
            'Category': item.get('Category', 'N/A'),
        }
        processed_data.append(processed_item)
    return processed_data


# --------- Data Cleaning Functions --------- #

def remove_duplicate_cricbuzz_data(processed_data):
    # Removing duplicates based on 'MatchName' and 'Venue'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['MatchName', 'Venue'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_cricket_news_info(processed_data):
    # Removing duplicates based on 'Headline'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['Headline'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_team_stats(processed_data):
    # Removing duplicates based on 'Name' and 'Game'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['Name', 'Game'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_player_stats(processed_data):
    # Removing duplicates based on 'Name', 'Country', and 'Game'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['Name', 'Country', 'Game'], keep='first')
    return df_no_duplicates.to_dict(orient='records')


# --------- Data Type Conversion Functions --------- #

def convert_data_types_team_stats(processed_data):
    # Convert 'Rating' and 'Points' to numeric type
    for item in processed_data:
        item['Rating'] = pd.to_numeric(item['Rating'], errors='coerce')
        item['Points'] = pd.to_numeric(item['Points'], errors='coerce')
    return processed_data

def convert_data_types_player_stats(processed_data):
    # Convert 'Rating' to numeric type
    for item in processed_data:
        item['Rating'] = pd.to_numeric(item['Rating'], errors='coerce')
    return processed_data


# --------- Data Standardization Functions --------- #


def standardize_formats_cricbuzz_data(processed_data):
    # Standardize 'Venue' format
    for item in processed_data:
        item['Venue'] = re.sub(r'\bStadium\b', 'Stad.', item['Venue'])
    return processed_data


def standardize_formats_team_stats(processed_data):
    # Standardize 'Game' format to uppercase
    for item in processed_data:
        item['Game'] = item['Game'].upper()
    return processed_data

def standardize_formats_player_stats(processed_data):
    # Standardize 'Country' format to uppercase
    for item in processed_data:
        item['Country'] = item['Country'].upper()
    return processed_data
