import requests
import re

url = 'https://news.yahoo.co.jp/articles/d7f6109e9acf32bfaa35fd6cf66690b159ad3b26/comments?page=19&t=t&order=recommended'
html = requests.get(url)
print(html.text)
