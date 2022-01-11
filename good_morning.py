import requests
import datetime

dt = datetime.datetime.now()
print(dt)

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
data = requests.get(url)
print(data)