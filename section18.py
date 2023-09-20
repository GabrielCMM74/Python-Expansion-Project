import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
print(res)  # res.text would give the full html
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')
href = soup.select('a')


def create_custom_hn(links, subtext, href):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn
# print(votes[0].get('id'))
# print(soup.select('.titleline'))  # now this is an object and we can manipulate it


pprint.pprint(create_custom_hn(links, subtext, href))
