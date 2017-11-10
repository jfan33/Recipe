import urllib.request as ur
import re
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from string import ascii_lowercase

'''
urls = ["http://www.unconventionalbaker.com/all-recipes/", "http://fitfoodiefinds.com/category/snacks-2/bars-balls-and-granola/page/5/"]

http://www.mydarlinglemonthyme.com/2016/06/flourless-chocolate-cake-with-matcha.html
http://www.thefullhelping.com/recipes/?fwp_small_plates=snacks
http://www.foodheavenmadeeasy.com/recipes/
http://minimalistbaker.com/recipes/sweet-things/
http://amygreen.me/recipes/#cb
http://www.elephantasticvegan.com/20-vegan-refined-sugar-free-desserts/
http://www.trinityskitchen.com/blueberry-lemon-fudge-with-creamed-coconut-4-ingredients/
http://fitfoodiefinds.com/category/snacks-2/bars-balls-and-granola/page/5/
http://www.101cookbooks.com/archives/savory-doityourself-power-bars-recipe.html






i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i<len(urls):
	htmlfile = ur.urlopen(urls[i])
	soup = BeautifulSoup(htmlfile, "html.parser")
	#htmltext = htmlfile.read().decode('utf-8')
	#titles = re.findall(pattern,htmltext)
	print(soup.title.text)
	i+=1



	for link in soup.findAll('a'):
	print(link.get('href'))
	print(link.text)


print(soup.findAll('a')[0])
print(soup.find('div',{"class": "jig-overflow"}))


for letter in ascii_lowercase:
'''

def make_soup(urls):
	thepage = ur.urlopen(urls)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

soup = make_soup("http://www.unconventionalbaker.com/all-recipes/")

i=1
for img in soup.findAll('img'):
	temp=img.get('src')
	if temp[:1]=="/":
		image = "http://www.unconventionalbaker.com/all-recipes/" + temp
	else:
		image=temp
	nametemp=img.get('alt')
	if len(nametemp)==0:
		filename=str(i)
		i+=1
	else:
		filename=nametemp

	imagefile=open(filename + ".jpeg", 'wb')
	imagefile.write(ur.urlopen(image).read())
	imagefile.close()

boundaries=[(255,20,147),([253, 246, 250])]

for (lower, upper) in boundaries:
	lower = np.array(lower, dtype="uint8")
	upper = np.array(upper, dtype="uint8")
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask=mask)

	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)





