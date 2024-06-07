from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_weather(city_name):
    try:
        translator = Translator()
        translated_city = translator.translate(city_name, src='ru', dest='en').text.lower()
        
        link = f"https://pogoda.mail.ru/prognoz/{translated_city}/24hours/"
        res = requests.get(link)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        
        temperature = soup.find(class_="p-forecast__temperature-value").get_text()
        weather = soup.find(class_="p-forecast__description").get_text()
        data = soup.find(class_="p-forecast__title").get_text()
        feelings = soup.find_all(class_="p-forecast__data")[0].get_text()
        pressure = soup.find_all(class_="p-forecast__data")[1].get_text()
        wind_speed = soup.find_all(class_="p-forecast__data")[2].get_text()
        humidity = soup.find_all(class_="p-forecast__data")[3].get_text()
        
        print(f"Сегодня: {temperature}, {weather}")
        print(f"Ощущается как: {feelings}")
        print(f"Давление: {pressure}")
        print(f"Скорость ветра: {wind_speed}")
        print(f"Влажность: {humidity}")
        print(data)
    except Exception as e:
        print("Произошла ошибка при получении данных о погоде.")
        print(f"Ошибка: {e}")

city_name = input("Введите название города: ")
get_weather(city_name)
TEST = input()
