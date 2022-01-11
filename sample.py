
from selenium import webdriver
import chromedriver_binary
import openpyxl
from time import sleep

urls = [
    'https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&sort=lost_points&order=desc&page=1&type=t&topic_id=20211228-00125292-wedge&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Farticlemain%3Fd%3D20211228-00125292-wedge-cn&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F96.0.4664.55%20Safari%2F537.36',
    "https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&page=2&sort=lost_points&order=desc&type=t&topic_id=20211228-00125292-wedge&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Farticlemain%3Fd%3D20211228-00125292-wedge-cn&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F96.0.4664.55%20Safari%2F537.36",
    'https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&page=3&sort=lost_points&order=desc&type=t&topic_id=20211228-00125292-wedge&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Farticlemain%3Fd%3D20211228-00125292-wedge-cn&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F96.0.4664.55%20Safari%2F537.36',
    'https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fnews.yahoo.co.jp&page=4&sort=lost_points&order=desc&type=t&topic_id=20211228-00125292-wedge&space_id=2079510507&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Farticlemain%3Fd%3D20211228-00125292-wedge-cn&comment_num=10&ref=&bkt=&flt=2&grp=&opttype=&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&mtestid=&display_blurred_comment=off&ua=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F96.0.4664.55%20Safari%2F537.36'
]
comment_selector = '.commentListItem .cmtBody'
file_name = './nakamuranokadai.xlsx'
sheet_name = 'Sheet1'

comments = []
driver = webdriver.Chrome()
for url in urls:
    driver.get(url)
    comment_elements = driver.find_elements_by_css_selector(comment_selector)
    for elem in comment_elements:
        comments.append(elem.text)

print(comments)

driver.close()

book = openpyxl.load_workbook(file_name)
sheet = book[sheet_name]
for i in range(len(comments)):
    sheet['A'+str(i+1)] = comments[i]

book.save(file_name)
