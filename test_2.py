from PIL import Image
import pyocr

pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

tools = pyocr.get_available_tools()
tool = tools[0]
txt = tool.image_to_string(Image.open('129.png'), lang="eng")

print(txt)