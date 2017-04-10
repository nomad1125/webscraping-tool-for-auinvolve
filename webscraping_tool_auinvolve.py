# Title: webscraping_tool_auinvolve.py
# Description: Designed specifically to scrape roster from auinvolve
# Author: Jarrett Tang
# Email: jkt0011@auburn.edu

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://auburn.collegiatelink.net/organization/ewb/roster'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# setting up soup recipe
page_soup = soup(page_html, "html.parser")

# grabbing soup ingredients
firstContainers = page_soup.findAll("tr",{"class" : "gridrow"})
secondContainer = page_soup.findAll("tr",{"class" : "gridrow_alternate"})
