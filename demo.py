from bs4 import BeautifulSoup
import urllib

soup = BeautifulSoup(urllib.urlopen('http://www.medline.com/catalog/category-products.jsp?iclp=cat1790004&N=105899&itemId=cat1790004&No=24'))

for prod in soup.find_all("div","medGridProdTitle"):
	for string in prod.stripped_strings:
		print(repr(string))

