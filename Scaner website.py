import requests
import socket
from bs4 import BeautifulSoup
import whois
def get_ip_address(url):
    try:
        id_address = socket.gethostbyname(url)
        return id_address
    except socket.gaierror:
        return None

def get_creation_date(url):
    try:
        domain = whois.whois(url)
        if isinstance(domain.creation_date, list):
            return domain.creation_date[0]
        else:
            return domain.creation_date
    except (whois.parser.PywhoisError, TypeError):
        return None

def scan_website(url):
    print("[+] Начинаем сканирование веб сайта:", url)

    ip_address = get_ip_address(url)
    if ip_address:
        print("[+] IP-адрес сайта:", ip-address)
    else:
        print("[-] Не удалось определить IP-адрес сайта")

    creation_date = get_creation_date(url)
    if creation_date:
        print("[+] Примерная дата создания сайта:", creation_date)
    else:
        print("[-] Не удалось определить дату создания сайта")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("[+] Веб-сайт доступен")
        else:
            print("[-] Веб-сайт недоступен")
            return
    except requests.ConnectionError:
        print("[-] Сайт недоступен")
        return

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        if "<script>" in response.text:
            print("[-] Обнаружен потенциальный XSS в странице:", url)
        
        if "SQL syntax" in response.text:
            print("[-] Обнаружен уязвимый SQL-инъекции в странице:", url)
        
        links = soup.find_all("a")
        external_links = []
        for link in links:
            href = link.get("href")
            if href.startswith("http"):
                external_links.append(href)
        print("[+] Найдено", len(external_links), "внешних ссылок на странице", url)
        if len(external_links) > 5:
            for i in range(5):
                print("[+] Внешняя ссылка:", external_links[i])
            print("[+] И еще", len(external_links) - 5, "ссылок")
        else:
            for link in external_links:
                print("[+] Внешняя ссылка:", link)
    
    except requests.ConnectionError:
        print("[-] Сайт недоступен")

if __name__ == "__main__":
    url = input("Введите URL для сканирования: ")
    scan_website(url)
    TEST = input()