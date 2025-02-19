# openweather api로 요청을 해서 그 결과를 csv로 저장하는 .py
import requests
import csv
from datetime import datetime
import os

API_KEY=os.getenv("OPENWEATHER_API_KEY")
CITY="Seoul"
URL=f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response=requests.get(URL)
data=response.json()

temp=data["main"]["temp"]
humi=data["main"]["humidity"]
weather=data["weather"][0]["description"]


timezone=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# csv 파일 생성
csv_filename="seoul_weather.csv"

header=["timezone", "temp", "humidity", "weather"]

# csv가 존재하면 -> True, 존재하지 않으면 -> False
file_exist=os.path.isfile(csv_filename)

# mode ="a" 
# => if not is file : create
# => if is file : write
with open(csv_filename, "a", newline="") as file:
    writer= csv.writer(file)
    if not file_exist:
        writer.writerow(header)
    writer.writerow([timezone, temp, humi, weather])
