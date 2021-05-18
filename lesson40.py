# Parsing HTML with the beautiful soup Module

import bs4
import requests

res = requests.get('https://automatetheboringstuff.com/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elem = soup.select('body > div.main > div:nth-child(1) > blockquote:nth-child(6)')

print(elem[0].text.strip())


