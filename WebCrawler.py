from html.parser import HTMLParser
from urllib.request import urlopen
from irllib import parser

class LinkParser(HTMLParser):

	def handle_starting(self, tag, attrs):
		# We are looking for the begining of a link. Links normally look like <a>
		if tag == 'a':
			for (key,value) in attrs:
				if key == 'href':
					newUrl = parse.urljoin(self.baseUrl, value)
					self.links = self.links + [newUrl]

	def getLinks(self, url):
		self.links = []
		self.baseUrl = url
		response = urlopen(url)
		if response.getheader('Content-Type') == 'text/html':
			htmlBytes = response.read()
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]


	def spider(url, word, maxPages):
		
		pagesToVisit = [url]
		numberVisited = 0
		foundWord = False
		
		# The main loop. Create a LinkParser and get all the links on the page.
		while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
			numberVisited = numberVisited + 1
			url = pagesToVisit[0]
			pagesToVisit = pagesToVisit[1:]
			try:
				print(numberVisited, "Visiting:", url)
				parser = LinkParser()
				data, links = parser.getLinks(url)
				if data.find(word) > -1:
					foundWord = True
					pagesToVisit = pagesToVisit + links
					print(" **Success!** ")

			except:
				print(" **Failed!** ")

		if foundWord:
			print("The word ", word, " was found at ", url)
		else:
			print("Word never found")


