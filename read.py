import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.mtl.org/en/what-to-do'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

div_read_post_list = soup.find('div', class_='read_post_list tabs_content')


if div_read_post_list:
    print(div_read_post_list.text.strip())
else:
     print("Div não encontrada.")
