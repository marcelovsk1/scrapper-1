import requests
from bs4 import BeautifulSoup

response = requests.get('https://ge.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

postNews = site.find('div', attrs={'class': 'feed-post-body'})

print(postNews.prettify())
