import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
#import csv

import time

options = Options()
options.add_argument('--headless=new')

home_directory = os.path.expanduser('~')
download_directory = os.path.join(home_directory, 'Downloads')
chrome_tool = os.path.join(download_directory, 'chromedriver-mac-x64/chromedriver')

text_file_path = os.path.join(home_directory,'Desktop')

service = Service(executable_path=chrome_tool)
driver = webdriver.Chrome(service=service, options=options)


driver.get('https://www.espncricinfo.com/rankings/content/page/211271.html')
time.sleep(5)

data = driver.find_elements(By.CLASS_NAME, 'StoryengineTable')

data1 = data[0].text.split('\n')
data2 = data[1].text.split('\n')
data3 = data[2].text.split('\n')
# data4 = data[3].text.split('\n')
# data5 = data[4].text.split('\n')

def Convert(string):
    li = list(string.split(" "))
    return li

def stuff_data(d123):
    country_beginnings = ['New', 'West', 'South', 'Sri', 'Hong', 'Saudi', 'Cayman', 'Isle', 'Czech', 'Cook', 'Sierra']

    l1 = []

    for a in d123:
        if isinstance(a, str):
            b = Convert(a)
            if len(b) > 5:
                for cb in country_beginnings:
                    if cb in b:
                        ind = b.index(cb)
                        b[ind] = b[ind]+' '+b[ind+1]
                        b.pop(ind+1)
            l1.append(b)
    return [item for sublist in l1 for item in sublist]

d1 = stuff_data(data1[2:])
d2 = stuff_data(data2[2:])
d3 = stuff_data(data3[2:])
# d4 = stuff_data(data4[2:])
# d5 = stuff_data(data5[2:])

nl = [d1, d2, d3]

def combine_stuff(data_for_columns):
    num_columns = 5
    reshaped_data = [data_for_columns[i:i + num_columns] for i in range(0, len(data_for_columns), num_columns)]
    return pd.DataFrame(reshaped_data, columns=['Pos', 'Team', 'Matches', 'Pts', 'Rating'])


for c in nl:
    print(combine_stuff(c))
