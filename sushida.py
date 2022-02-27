from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
from PIL import Image
import pyocr
import pyocr.builders

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

url = "http://typingx0.net/sushida"
driver = webdriver.Chrome()
tools = pyocr.get_available_tools()
tool = tools[0]
builder = pyocr.builders.TextBuilder()

driver.get(url)
time.sleep(3)

driver.find_element(by=By.XPATH, value='//div[@class="main_play"]/a').click()
time.sleep(10)

actions = ActionChains(driver)
actions.move_by_offset(500, 380).click().perform()
time.sleep(5)

actions.move_by_offset(0, 70).click().perform()

time.sleep(3)

actions.send_keys(" ").perform

time.sleep(2)

for i in range(340):
    driver.save_screenshot('screenshot.png')
    image = Image.open('screenshot.png')
    cropped = image.crop((500,540,1000,580)).convert('L').point(lambda x: 255 if x < 150 else 0)
    cropped.save('cropped.png')
    text = tool.image_to_string(cropped, lang="eng", builder=builder)
    actions.send_keys(text).perform()
    

time.sleep(5)

driver.close()
driver.quit()
