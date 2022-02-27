from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_binary
import openpyxl
import urllib.parse
import time

keyword = "中古バイク"
enc = urllib.parse.quote(keyword)
url = f"https://news.yahoo.co.jp/search?p={enc}&ei=utf-8"
driver = webdriver.Chrome()
driver.get(url)
name_selector = '.newsFeed_item_title'
link_selector = '.newsFeed_item_link'
article_names = driver.find_elements(by=By.CSS_SELECTOR, value=name_selector)
article_links = driver.find_elements(by=By.CSS_SELECTOR, value=link_selector)

for i in range(len(article_names)):
    article_names[i] = article_names[i].text
    print(f"{i+1}. {article_names[i]}")
    article_links[i] = article_links[i].get_attribute('href')
    print(f" {article_links[i]}")

print("どの記事を参照しますか？")
driver.close()

n = int(input())
article_name = article_names[n-1]
article_link = article_links[n-1]

file_name = f'{article_name}.xlsx'
sheet_name = 'Sheet'
comments = []
driver = webdriver.Chrome()
i = 1
while True:
    if i == 8:
        break
    url = f"{article_link}/comments?page={i}&t=t&order=recommended"
    driver.get(url)
    iframe = driver.find_element(by=By.CSS_SELECTOR, value='.news-comment-plguin-iframe')
    src = iframe.get_attribute('src')
    driver.get(src)
    comment_elements = driver.find_elements(by=By.CSS_SELECTOR, value='.cmtBody')
    for elem in comment_elements:
        comments.append(elem.text)
    i += 1

try:
    book = openpyxl.load_workbook(file_name)
except FileNotFoundError:
    book = openpyxl.Workbook()
sheet = book[sheet_name]

for i in range(len(comments)):
    sheet['A'+str(i+1)] = comments[i]

book.save(file_name)

driver.close()

url = "https://textmining.userlocal.jp"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

driver.find_element(by=By.CSS_SELECTOR, value="li.nav-item:nth-child(2)").click()
driver.find_element(by=By.XPATH, value='//input[@name="document1[file]"]').send_keys(f"C:\\Users\\ryuta\\OneDrive\\ドキュメント\\VSCode\\Python\\{article_name}.xlsx")
driver.find_element(by=By.XPATH, value='//input[@value="テキストマイニングする"]').click()

time.sleep(2)
driver.execute_script("window.scrollTo(0, 200);")
driver.find_element(by=By.XPATH, value='//button[@class="ml-2 close"]').click()
png = driver.find_element(by=By.XPATH, value='//div[@class="result-frame ul-d3-chart"]').screenshot_as_png

with open('./screenshot.png', 'wb') as f:
    f.write(png)

time.sleep(5)

driver.close()