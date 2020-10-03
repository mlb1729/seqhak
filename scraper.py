# scraper TEST
# print("Hello Scraper!")

import requests
from bs4 import BeautifulSoup

# helper to extract just the host info from an HTML item
def hostFromHTMLItem(item):
	atag = item.contents[0]
	path = atag["href"]
	split = path.split("/")
	host = split[-1]
	return host

# this returns a Python dictionary homologrous to a JSON object with 
# 	"merchantHost": the merchant host
# 	"similarHosts": a list of similar-store hosts
def scrapeSimilarHosts(merchantHost):

	url = "https://givingassistant.org/coupon-codes/" + merchantHost	# ToDo: magic constant string

	page = requests.get(url)

	status = page.status_code

	# ToDo: make this a real exception catch
	# if (status == 200):
	# 	print("Got page!")
	# else:
	# 	print("Bad page get status: " + str(status))

	parsedHTML = BeautifulSoup(page.text, "html.parser")

	# this would be fragile if there were other such elements on the page
	# better would be to navigate to just that section
	htmlItems = parsedHTML.find_all(class_="col-sm-4 center")	# ToDo: magic constant string

	similarHosts = [hostFromHTMLItem(item) for item in htmlItems]

	result = {"merchantHost": merchantHost, "similarHosts": similarHosts}

	return result

# demo
result = scrapeSimilarHosts("homedepot.com")
print(result)

result = scrapeSimilarHosts("kmart.com")
print(result)
