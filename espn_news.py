import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#import pandas as pd
#import csv

import time

options = Options()
options.add_argument('--headless')

# home_directory = os.path.expanduser('~')
# download_directory = os.path.join(home_directory, 'Downloads')
# chrome_tool = os.path.join(download_directory, 'chromedriver-mac-x64/chromedriver')

# text_file_path = os.path.join(home_directory,'Desktop')

# service = Service(executable_path=chrome_tool)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome()


driver.get('https://www.espncricinfo.com/cricket-news')
time.sleep(5)

data = driver.find_elements(By.CLASS_NAME, 'ds-border-b.ds-border-line.ds-p-4')
for element in data:
    print(element.text)
