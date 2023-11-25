import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

print(response.content)
