from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_binary
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

driver.close()

url = "https://textmining.userlocal.jp"
driver = webdriver.Chrome()
driver.get(url)
actions = ActionChains(driver)

time.sleep(5)

for comment in comments:
    actions.send_keys(comment).perform()
    actions.send_keys(Keys.ENTER).perform()

time.sleep(3)
driver.find_element(by=By.XPATH, value='//input[@value="テキストマイニングする"]').click()

time.sleep(5)

driver.save_screenshot('screenshot.png')
driver.close()