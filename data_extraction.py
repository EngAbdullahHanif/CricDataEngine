import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This file contains the code for extracting data from Cricbuzz website using Python, Selenium, and Beautiful Soup

# ------------------ Extracting cricket match data -----------------

def extract_cricbuzz_data(pages_to_scrape=10):
    base_url = 'https://www.cricbuzz.com/cricket-series/6732/icc-cricket-world-cup-2023/matches'

    data_list = []

    for page in range(1, pages_to_scrape + 1):
        url = f'{base_url}?page={page}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            match_rows = soup.find_all('div', class_='cb-col-75 cb-col')
        
            for match_row in match_rows:

                match_name_elem = match_row.select_one('a.text-hvr-underline')
                match_name = match_name_elem.text.strip() if match_name_elem else ''

                venue_elem = match_row.select_one('div.text-gray')
                venue = venue_elem.text.strip() if venue_elem else ''

                result_elem = match_row.select_one('a.cb-text-complete')
                result = result_elem.text.strip() if result_elem else ''

                match_data = {
                    'match_name': match_name,
                    'venue': venue,
                    'result': result
                }
                data_list.append(match_data)

            print(f"Page {page} scraped successfully.")
        else:
            print(f"Failed to retrieve data from page {page}. Status Code: {response.status_code}")
    return data_list


# ----------------- Extracting cricket news -----------------


def extract_cricket_news_info(article_urls):
    data_list = []

    for article_url in article_urls:
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_elem = soup.find('h1', class_='nws-dtl-hdln')
            headline = headline_elem.text.strip() if headline_elem else 'N/A'

            content_elements = soup.find_all('section', class_='cb-nws-dtl-itms')
            # the content_elements is a list of all the elements with the class cb-nws-dtl-itms, so we need to iterate over it to get the text of each element
            content = ' '.join([content_elem.text.strip() for content_elem in content_elements])
        
            article_info = []
            article_info = soup.find_all('div', class_='cb-nws-sub-txt')

            # author_elem = article_info.find('span', itemprop='name')
            author_elem = article_info[1].find('span', itemprop='name')
            author = author_elem.text.strip() if author_elem else 'N/A' 


            date_elem = article_info[1].find('time', itemprop='dateModified')['datetime'] if soup.find('time', itemprop='dateModified') else None
            publication_date = datetime.strptime(date_elem, "%b %d %a %Y %Z %H:%M:%S %f").strftime('%d/%m/%Y') if date_elem else 'N/A'

            data_list.append({
                'headline': headline,
                'content': content,
                'author': author,
                'publication_date': publication_date
            })  

            print(f"Article {article_url} scraped successfully.")

        else:
            print(f"Failed to retrieve data. Status Code: {response.status_code}")
    
    return data_list


# ----------------- Extracting team stats -----------------


def extract_team_stats(driver, stats_url, game_type):
    extracted_data = []

    driver.get(stats_url)

    if game_type == 'ODI':
        # Now click on the desired element
        driver.find_element(By.ID, 'teams-odis-tab').click()
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cb-col.cb-col-100.cb-padding-left0.ng-hide'))
        WebDriverWait(driver, 5).until(element_present)

    elif game_type == 'T20':
        driver.find_element(By.ID, 'teams-t20s-tab').click()
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cb-col.cb-col-100.cb-padding-left0.ng-hide'))
        WebDriverWait(driver, 5).until(element_present)
    

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    table = soup.find('div', class_='cb-col cb-col-100 cb-padding-left0')
    for row in table.find_all('div', class_='cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center'):

        position = row.find('div', class_='cb-col cb-col-20 cb-lst-itm-sm')
        name = row.find('div', class_='cb-col cb-col-50 cb-lst-itm-sm text-left')
        rating = row.find('div', class_='cb-col cb-col-14 cb-lst-itm-sm')
   
        points_divs = row.find_all('div', class_='cb-col cb-col-14 cb-lst-itm-sm')
        if len(points_divs) >= 2:
            points = points_divs[1]
        else:
            points = "N/A"

        extracted_data.append({
            'position': position.text,
            'name': name.text,
            'rating': rating.text,
            'points': points.text,
            'game_type': game_type,
        })

    return extracted_data


# ----------------- Extracting player stats -----------------


def extract_player_stats(driver, stats_url, game_type, category):
    extracted_data = []

    driver.get(stats_url)

    if game_type != 'TEST':
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cb-col.cb-col-100.cb-padding-left0'))
        WebDriverWait(driver, 10).until(element_present)

    elif game_type == 'ODI':
        driver.find_element(By.ID, 'batsmen-odis-tab').click()
        # element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cb-col.cb-col-100.cb-padding-left0.ng-hide'))
        WebDriverWait(driver, 5).until(element_present)

    elif game_type == 'T20':
        driver.find_element(By.ID, 'batsmen-t20s-tab').click()
        # element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cb-col.cb-col-100.cb-padding-left0.ng-hide'))
        # WebDriverWait(driver, 5).until(element_present)
      

    print(f"Successfully clicked on {game_type} {category} tab")

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    table = soup.find('div', class_='cb-col cb-col-100 cb-padding-left0')
 
    for row in table.find_all('div', class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center'):
        position = row.find('div', class_='cb-col cb-col-16 cb-rank-tbl cb-font-16')
        player_name = row.find('a', class_='text-hvr-underline')
        country_name = soup.find('div', class_='cb-font-12 text-gray')


        # name = row.find('div', class_='cb-col cb-col-50 cb-lst-itm-sm text-left')
        rating = row.find('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right')
   
        extracted_data.append({
            'position': position.text,
            'name': player_name.text,
            'country': country_name.text,
            'rating': rating.text,
            'game_type': game_type,
            'category': category,
        })

    return extracted_data
