import requests
import os

def download_image(url, save_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        file_extension = url.split('.')[-1].lower()
        if file_extension in ['png', 'jpg']:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Файл успешно скачан и сохранен как", save_path)
        else:
            print("Недопустимый формат файла. Разрешены только PNG и JPG.")
    else:
        print("Не удалось скачать файл. Код ошибки:", response.status_code)

url = input("Введите вашу ссылку: ")
save_path = "downloaded_image.png"
download_image(url, save_path)
