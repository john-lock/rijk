from random import randint
import json, requests

def get_random_art():
	APIKEY ='9UogSlO5'
	P = str(randint(1,10000))
	link = "https://www.rijksmuseum.nl/api/en/collection/?key=" + APIKEY + "&format=json&imgonly=True&ps=1&p=" + P
	art = requests.get(link)
	ob = json.loads(art.text)
	print(ob['artObjects'][0]['webImage']['url'])
	# need to refactor
	# should also grab info like Artist, Name, etc..

get_random_art()


