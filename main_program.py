from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from data_extraction import extract_cricbuzz_data, extract_cricket_news_info, extract_team_stats, extract_player_stats
from data_processing import (convert_data_types_team_stats, convert_data_types_player_stats,
    standardize_formats_cricbuzz_data, standardize_formats_team_stats, standardize_formats_player_stats
)
from data_io import save_to_csv
from news_article_urls import news_article_urls

directory = 'data'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

# extract cricbuzz data
cricbuzz_data = extract_cricbuzz_data(20)
print(f"scraped successfully for cricbuzz_data")


# extract news article info
cricket_news_info = extract_cricket_news_info(news_article_urls)
print(f"scraped successfully for cricket_news_info")



# extract team stats
stats_urls = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/teams'
extracted_data_test = extract_team_stats(driver, stats_urls, 'TEST')
print(f"scraped successfully for TEST")
extracted_data_odi = extract_team_stats(driver, stats_urls, 'ODI')
print(f"scraped successfully for ODI")
extracted_data_t20 = extract_team_stats(driver, stats_urls, 'T20')
print(f"scraped successfully for T20")
team_stats_data = extracted_data_test + extracted_data_odi + extracted_data_t20



#  extract player stats
stats_urls_batting = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting'
stats_urls_bowling = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling'
stats_urls_all_rounder = 'https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder'

extracted_data_batting_test = extract_player_stats(driver, stats_urls_batting, 'TEST', 'Batting')
print(f"Scraped successfully for TEST Batting")


extracted_data_bowling_test = extract_player_stats(driver, stats_urls_bowling, 'TEST', 'Bowling')
print(f"Scraped successfully for TEST Bowling")


extracted_data_all_rounder_test = extract_player_stats(driver, stats_urls_all_rounder, 'TEST', 'All-Rounder')
print(f"Scraped successfully for TEST All-Rounder")


extracted_data_batting_odi = extract_player_stats(driver, stats_urls_batting, 'ODI', 'Batting')
print(f"Scraped successfully for ODI Batting")


extracted_data_bowling_odi = extract_player_stats(driver, stats_urls_bowling, 'ODI', 'Bowling')
print(f"Scraped successfully for ODI Bowling")


extracted_data_all_rounder_odi = extract_player_stats(driver, stats_urls_all_rounder, 'ODI', 'All-Rounder')
print(f"Scraped successfully for ODI All-Rounder")


extracted_data_batting_t20 = extract_player_stats(driver, stats_urls_batting, 'T20', 'Batting')
print(f"Scraped successfully for T20 Batting")


extracted_data_bowling_t20 = extract_player_stats(driver, stats_urls_bowling, 'T20', 'Bowling')
print(f"Scraped successfully for T20 Bowling")

extracted_data_all_rounder_t20 = extract_player_stats(driver, stats_urls_all_rounder, 'T20', 'All-Rounder')
print(f"Scraped successfully for T20 All-Rounder")


player_stats_data = extracted_data_batting_test + extracted_data_bowling_test + extracted_data_all_rounder_test + extracted_data_batting_odi + extracted_data_bowling_odi + extracted_data_all_rounder_odi + extracted_data_batting_t20 + extracted_data_bowling_t20 + extracted_data_all_rounder_t20



driver.quit()

# Convert Data Types
team_stats_data = convert_data_types_team_stats(team_stats_data)
player_stats_data = convert_data_types_player_stats(player_stats_data)

# Standardize Formats
cricbuzz_data = standardize_formats_cricbuzz_data(cricbuzz_data)
team_stats_data = standardize_formats_team_stats(team_stats_data)
player_stats_data = standardize_formats_player_stats(player_stats_data)

if not os.path.exists(directory):
    os.makedirs(directory)

cricbuzz_data_file_path = 'data/cricbuzz_data.csv'
cricket_news_info_file_path = 'data/cricket_news_info.csv'
team_stats_data_file_path = 'data/team_stats_data.csv'
player_stats_data_file_path = 'data/player_stats_data.csv'

save_to_csv(cricbuzz_data, cricbuzz_data_file_path)
save_to_csv(cricket_news_info, cricket_news_info_file_path)
save_to_csv(team_stats_data, team_stats_data_file_path)
save_to_csv(player_stats_data, player_stats_data_file_path)
