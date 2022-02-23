from selenium import webdriver
import chromedriver_binary
import requests
import re
import openpyxl
import urllib.parse

keyword = "中古バイク"
enc = urllib.parse.quote(keyword)
url = f"https://news.yahoo.co.jp/search?p={enc}&ei=utf-8"
html = requests.get(url)
pattern = '<div class="newsFeed_item_title">(.+?)<\/div>'
article_names = re.findall(pattern, html.text)
pattern = 'newsFeed_item_link" href="(.+?)"'
article_urls = re.findall(pattern, html.text)

for i in range(len(article_names)):
    print(f"{i+1}. {article_names[i]}")

print("どの記事を参照しますか？")
n = int(input())
article_name = article_names[n-1]

file_name = f'./{article_name}.xlsx'
sheet_name = 'Sheet'
comments = []
names = []
dates = []
agrees = []
disagrees = []

comment_pattern = '<span class="cmtBody">(.+)<\/span>'
name_pattern = '<h1 class="name yjxName">.+class="rapidnofollow">(.+)<\/a>'
date_pattern = 'pubdate>\s+(.+)'
agree_pattern = 'good votes-btn.+\s\s.+<span class="userNum">(.+)<\/span>'
disagree_pattern = 'bad votes-btn.+\s\s.+<span class="userNum">(.+)<\/span>' 

driver = webdriver.Chrome()
i = 1
while True:
    article_url = f"{article_urls[n-1]}/comments?page={i}&t=t&order=recommended"
    driver.get(article_url)
    iframe = driver.find_element_by_class_name("news-comment-plguin-iframe")
    src = iframe.get_attribute('src')
    html = requests.get(src)
    if re.search('この記事にはまだコメントがありません。', html.text):
        print("Done")
        break
    comment_elements = re.findall(comment_pattern, html.text)
    comment_elements.pop()
    comment_elements = [re.sub('<br \/>','',element) for element in comment_elements]
    name_elements = re.findall(name_pattern, html.text)
    date_elements = re.findall(date_pattern, html.text)
    agree_elements = re.findall(agree_pattern, html.text)
    disagree_elements = re.findall(disagree_pattern, html.text)

    comments += comment_elements
    names += name_elements
    dates += date_elements
    agrees += agree_elements
    disagrees += disagree_elements
    i += 1

try:
    book = openpyxl.load_workbook(file_name)
except FileNotFoundError:
    book = openpyxl.Workbook()
sheet = book[sheet_name]
sheet['A'+str(1)] = "日付"
sheet['B'+str(1)] = "名前"
sheet['C'+str(1)] = "good"
sheet['D'+str(1)] = "bad"
sheet['E'+str(1)] = "コメント"

for i in range(len(comments)):
    sheet['A'+str(i+3)] = dates[i]
    sheet['B'+str(i+3)] = names[i]
    sheet['C'+str(i+3)] = agrees[i]
    sheet['D'+str(i+3)] = disagrees[i]
    sheet['E'+str(i+3)] = comments[i]

book.save(file_name)