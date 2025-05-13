import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Настраиваем argparse
parser = argparse.ArgumentParser(description="Извлечение внешних ссылок с веб-страницы")
parser.add_argument("--url", required=True, help="URL страницы для парсинга")
args = parser.parse_args()

# Получаем URL из аргументов
url = args.url

# Устанавливаем заголовки, чтобы сайт не блокировал скрипт
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# Узнаем домен сайта, чтобы в дальнейшем отфильтровать по нему ненужные ссылки
domain = urlparse(url).netloc

# Получаем HTML той страницы, которую хотим распарсить
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

external_links = []

for link in soup.find_all('a', href=True):
    href = link['href']

    # Преобразуем в абсолютный URL все ссылки, чтобы относительные ссылки тоже можно было отфильтровать по домену
    full_url = urljoin(url, href)

    #Извлекаем домен из каждой ссылки
    link_domain = urlparse(full_url).netloc

    # Проверяем, отличается ли этот домен от домена сайта, который мы парсим. Если да, то это внешняя ссылка
    if link_domain and link_domain != domain:
        external_links.append(full_url)

# Пользователь выбирает: вывести в консоль или сохранить в файл
choice = input("Что вы хотите сделать?\n"
               "1 - Вывести ссылки в консоль\n"
               "2 - Сохранить ссылки в файл\n"
               "Введите 1 или 2: ")

if choice == '1':
    for link in external_links:
        print(link)
else:
    with open('external_links.txt', 'w', encoding='utf-8') as f:
        for link in external_links:
            f.write(link + '\n')

