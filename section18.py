import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res)  # res.text would give the full html
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body)  # now this is an object and we can manipulate it
