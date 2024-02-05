import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import csv

import time

options = Options()
options.add_argument('--headless=new')

home_directory = os.path.expanduser('~')
download_directory = os.path.join(home_directory, 'Downloads')
chrome_tool = os.path.join(download_directory, 'chromedriver-mac-x64/chromedriver')

text_file_path = os.path.join(home_directory,'Desktop')

service = Service(executable_path=chrome_tool)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.espncricinfo.com/records/year/team-match-results/2023-2023/one-day-internationals-2')
time.sleep(5)

# result = driver.find_element(By.CLASS_NAME, 'ds-bg-fill-content-prime.ds-py-3.ds-px-4.ds-flex.ds-justify-between.ds-items-center')
# print(result.text)
 
teams = driver.find_elements(By.CLASS_NAME, 'ds-w-full.ds-table.ds-table-xs.ds-table-auto.ds-w-full.ds-overflow-scroll.ds-scrollbar-hide')
data = []

for team in teams:
    team_name = team.find_element(By.CLASS_NAME, 'ds-min-w-max')

    print('team_name: ', team_name.text)
    # data = team.text.split('\n')

'''
with open(new_filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Writing the data into the file
    for item in combined_list:
        writer.writerow(item)

new_filename'''

'''
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combined_list)
'''
