#python code that Prints out list of all Austronaunts in the Space for the current time being

import requests 
import json

#api to get the data
response = requests.get("http://api.open-notify.org/astros.json")
people = (response.json()['people'])

astro_list = []
craft_list =[]

for i in people:
	a= i.get('name')
	b= i.get('craft')
	astronaunts = astro_list.append(a) 
	creq_craft = craft_list.append(b)

#Print the Names & Craft as lists of Astronants out in Space 
#print(astro_list)
#print (craft_list)



'''in order to export it as Table representing Austronaunts' Craft and Name here we go
'''

import pandas as pd
astronaunt = pd.DataFrame(list(zip(craft_list,astro_list)), columns  = ['Craft','Name'])

print(astronaunt)
