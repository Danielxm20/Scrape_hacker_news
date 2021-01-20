import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
print(response) # codigo de repsuesta
#print(response.text) # documento obtenido

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
#print(soup.body)
#print(soup.find_all('div'))
#print(soup.find_all('a')) # muestra todos los links
print(soup.title)
print(soup.a) # la primera etiqueta a
print(soup.find('a')) # la primera etiqueta a
print(soup.find(id="score_25517868"))

print()

print(soup.select('.score')) # selector css de clase
print(soup.select("#score_25517868"))

links = soup.select('.storylink') # obtiene todos los links
votes = soup.select('.score') # obtiene todos los votos
#print(votes[0]) # imprime el primer elemento
