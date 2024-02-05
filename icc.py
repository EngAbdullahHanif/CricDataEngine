import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import itertools
import time
 
home_directory = os.path.expanduser('~')
download_folder = os.path.join(home_directory, 'Downloads')
chrome_driver = os.path.join(download_folder, 'chromedriver-mac-arm64/chromedriver')
 
options = Options()
options.add_argument('--headless=new')
 
service = Service(executable_path=chrome_driver)
 
driver = webdriver.Chrome(service=service, options=options)
 
# driver.get("https://www.icc-cricket.com/rankings/team-rankings/mens/odi")
# driver.get("https://www.icc-cricket.com/rankings/team-rankings/mens/test")
# driver.get("https://www.icc-cricket.com/rankings/team-rankings/mens/t20i")
# driver.get("https://www.icc-cricket.com/rankings/bowling/mens/test")
driver.get("https://www.icc-cricket.com/rankings/allrounder/mens/test")
 
# Find the parent element using class name
parent_elements = driver.find_element(By.CLASS_NAME, "waf-component.waf-dashboard.si-widget")
 
# print(f"stupid code: {parent_elements}")
time.sleep(3)
 
if parent_elements:
    # Extract text from the first parent element
    parent_text = parent_elements.text
    data = parent_text.split('\n')
    data1 = data[4:]
    data1.remove('1')
    data1.remove('1')
    data1.remove('1')
    data1.remove('1')
    data1.remove('1')
    data1.remove('1')
    data1.remove('3')
    # data1.remove('2')
    # # data1.remove('2')
else:
    print("Parent element not found.")
 
data_for_columns= data1
num_columns = 5
reshaped_data = [data_for_columns[i:i + num_columns] for i in range(0, len(data_for_columns), num_columns)]
df = pd.DataFrame(reshaped_data, columns=['Pos', 'Team', 'Matches', 'Pts', 'Rating'])
df.to_csv('Allrounder_Mens_Test.csv', index=False)
 
print(df)
 
 
  
driver.quit()