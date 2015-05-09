import urflparse
import urllib
from bs4 import BeatifulSoup

url = "http://nytimes.com,http://nytimes.com,http://nytimes.com"

urls = [url] # stack of urls to scrape
visited = [url] # historic record of urls


while len(urls) > 0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeatifulSoup(htmltext)

	urls.pop(0)

	for tag in soup.findAll('a',href=True):
		tab['href'] = urlparse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

print visited

