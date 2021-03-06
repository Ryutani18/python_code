import requests
import re
import openpyxl

file_name = './nakamuranokadai.xlsx'
sheet_name = 'Sheet1'
comments = []
pattern = '<span class="cmtBody">(.+)<\/span>'
i = 1
while True:
  url = f"https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&sort=lost_points&order=desc&page={i}&type=t&topic_id=20211228-00125292-wedge&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Farticlemain%3Fd%3D20211228-00125292-wedge-cn&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F96.0.4664.55%20Safari%2F537.36"
  html = requests.get(url)
  if re.search('この記事にはまだコメントがありません。', html.text):
    break
  comment_elements = re.findall(pattern, html.text)
  comment_elements.pop()
  for element in comment_elements:
    comments.append(re.sub('<br \/>','',element))
  i += 1

book = openpyxl.load_workbook(file_name)
sheet = book[sheet_name]
for i in range(len(comments)):
    sheet['A'+str(i+1)] = comments[i]

book.save(file_name)
