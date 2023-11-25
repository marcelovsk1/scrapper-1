import requests
from bs4 import BeautifulSoup

response = requests.get('https://ge.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML
postNews = site.find('div', attrs={'class': 'feed-post-body'})

#Title
title = postNews.find('a', attrs={'class': 'feed-post-link'})

print(title.text)
