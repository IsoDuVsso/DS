import requests

#URL de la page retournant le résultat, à adapter
url = 'http://localhost:8080/results'

#Requête avec valeur passé en dur 
r = requests.post(url,json={'niveau':5, 'ventes_trim1':200, 'ventes_trim2':400})

print(r.json())
