import requests
from pprint import pprint

url = "https://akabab.github.io/superhero-api/api/"
resp = requests.get(url + 'all.json')
list_hero = resp.json()
intellect = {}
heroes = ['Hulk', 'Captain America', 'Thanos']
for hero in list_hero:
    mind = hero['powerstats']['intelligence']
    name = hero['name']
    for n in heroes:
        if name == n:
            intellect[name] = mind
max_i = max(intellect, key = intellect.get)
print(max_i)