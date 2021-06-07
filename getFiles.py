import requests
import json

fdict = {}
with open("TomNJerry.json") as fin:
	fdict = json.load(fin)

dList = []
for e in fdict.keys(): dList.append(e)
dList.sort()

url = "https://www.cia.gov/library/abbottabad-compound"

for x in dList:
	with open("files/"+x, "wb") as file:
		print(url+fdict[x])
		response = requests.get(url+fdict[x])
		file.write(response.content)
