import requests
from bs4 import BeautifulSoup

page = requests.get("http://food.ndtv.com/recipe-sattu-parantha-816921")

soup =  BeautifulSoup(page.content , 'html.parser')


#print (soup.prettify())

#print type(soup)

ingredients = soup.find_all("div", class_="ingredients")

final_list = {}

for element in ingredients:
	final_list = ingredients[0].li.text
	print(final_list)
	print(type(final_list))
	