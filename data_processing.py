# data_processing.py
import pandas as pd
import re

# --------- Data Processing Functions --------- #

def process_cricbuzz_data(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'match_name': item.get('match_name', 'N/A'),
            'venue': item.get('venue', 'N/A'),
            'rsesult': item.get('result', 'N/A')
        }
        processed_data.append(processed_item)
    return processed_data

def process_cricket_news_info(data):
    # Handling missing values, converting data types, and text processing
    processed_data = []
    for item in data:
        processed_item = {
            'headline': item.get('headline', 'N/A'),
            'content': item.get('content', 'N/A'),
            'author': item.get('author', 'Unknown'),
            'publication_date': pd.to_datetime(item.get('publication_date', 'N/A'), errors='coerce').strftime('%Y-%m-%d')
        }
        processed_data.append(processed_item)
    return processed_data

def process_team_stats(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'position': item.get('position', 'N/A'),
            'name': item.get('name', 'N/A'),
            'rating': item.get('rating', 'N/A'),
            'points': item.get('points', 'N/A'),
            'game': item.get('game', 'N/A'),
        }
        processed_data.append(processed_item)
    return processed_data

def process_player_stats(data):
    # Handling missing values by replacing them with 'N/A'
    processed_data = []
    for item in data:
        processed_item = {
            'position': item.get('position', 'N/A'),
            'name': item.get('name', 'N/A'),
            'country': item.get('country', 'N/A'),
            'rating': item.get('rating', 'N/A'),
            'game_type': item.get('game_type', 'N/A'),
            'category': item.get('category', 'N/A'),
        }
        processed_data.append(processed_item)
    return processed_data


# --------- Data Cleaning Functions --------- #

def remove_duplicate_cricbuzz_data(processed_data):
    # Removing duplicates based on 'MatchName' and 'Venue'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['match_name', 'venue'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_cricket_news_info(processed_data):
    # Removing duplicates based on 'Headline'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['headline'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_team_stats(processed_data):
    # Removing duplicates based on 'Name' and 'Game'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['name', 'game'], keep='first')
    return df_no_duplicates.to_dict(orient='records')

def remove_duplicate_player_stats(processed_data):
    # Removing duplicates based on 'Name', 'Country', and 'Game'
    df = pd.DataFrame(processed_data)
    df_no_duplicates = df.drop_duplicates(subset=['name', 'country', 'game'], keep='first')
    return df_no_duplicates.to_dict(orient='records')


# --------- Data Type Conversion Functions --------- #

def convert_data_types_team_stats(processed_data):
    # Convert 'Rating' and 'Points' to numeric type
    for item in processed_data:
        item['rating'] = pd.to_numeric(item['rating'], errors='coerce')
        item['points'] = pd.to_numeric(item['points'], errors='coerce')
    return processed_data

def convert_data_types_player_stats(processed_data):
    # Convert 'Rating' to numeric type
    for item in processed_data:
        item['rating'] = pd.to_numeric(item['rating'], errors='coerce')
    return processed_data


# --------- Data Standardization Functions --------- #


def standardize_formats_cricbuzz_data(processed_data):
    # Standardize 'Venue' format
    for item in processed_data:
        item['venue'] = re.sub(r'\bStadium\b', 'Stad.', item['venue'])
    return processed_data


def standardize_formats_team_stats(processed_data):
    # Standardize 'Game' format to uppercase
    for item in processed_data:
        item['game_type'] = item['game_type'].upper()
    return processed_data

def standardize_formats_player_stats(processed_data):
    # Standardize 'Country' format to uppercase
    for item in processed_data:
        item['country'] = item['country'].upper()
    return processed_data
