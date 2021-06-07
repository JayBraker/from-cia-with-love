from bs4 import BeautifulSoup
import requests
import json
import re

toSearch = requests.get("https://www.cia.gov/library/abbottabad-compound/Video.20171021.hash_index.txt")
soup = BeautifulSoup(toSearch.content, 'html.parser')

final = []
for e in soup.contents[0].split("./"):
	if re.search("Tom",e):
		final.append("/"+e)

finalD = {}
for e in final:
	e = e.replace("\n","")
	r = e.split("_")
	r.remove(r[0])
	finalS = ""
	for i in r:
		finalS += i
	finalD[finalS] = e

with open("TomNJerry.json","w") as fout:
	json.dump(finalD,fout)
