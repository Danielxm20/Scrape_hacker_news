import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')


links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_new_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ' ')) # reemplaza el espacio vacio y points
            if points > 99:
                hn.append({'title':  title, 'link': href, 'votes': points})
    return sort_new_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
