# Title: webscraping_tool_auinvolve.py
# Description: Designed specifically to scrape roster from auinvolve
# Author: Jarrett Tang
# Email: jkt0011@auburn.edu

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# login function here

my_url = 'https://auburn.collegiatelink.net/organization/ewb/roster/members'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# setting up soup recipe
page_soup = soup(page_html, "html.parser")

# setting cooking timer for soup
def canContinue(page_check):
    paginationContainer = page_check.findAll("div", {"class" : "pagination"})
    strTemp = paginationContainer[0].span.text
    numTemp = [int(s) for s in strTestEnd.split() if s.isdigit()]
    if numTemp[2] - numTemp[1] > 0:
        return True

    return False;

# main loop
while canContinue(page_soup):
    #grabbing soup ingredients
    primaryContainers = page_soup.findAll("tr", {"class" : "gridrow"})
    partnerContainters = page_soup.findAll("tr", {"class" : "gridrow_alternate"})

    for primaryContainer in primaryContainers:
        
