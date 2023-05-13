import requests
from bs4 import BeautifulSoup

# Загрузка веб-страницы
url = 'https://www.google.com'
page = requests.get(url)

# Создание объекта BeautifulSoup из HTML-кода страницы
soup = BeautifulSoup(page.content, 'html.parser')

# Поиск элементов страницы
title = soup.find('title')
paragraphs = soup.find_all('p')

# Вывод найденных элементов
print(title.text)
for p in paragraphs:
    print(p.text)
