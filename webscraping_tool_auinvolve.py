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

# finding max cooking time for soup
def paginationLimit(page_check):
    paginationContainer = page_check.findAll("div", {"class" : "pagination"})
    str_temp = test_soup[0].a.next_sibling.next_sibling['href']
    page_number_location = len(str_temp) - 1
    ret_val = str_temp[page_number_location]
    return ret_val

# main loop
MAX_PAGE = paginationLimit(page_soup)
for page_index in range(1, MAX_PAGE):

while canContinue(page_soup):
    #grabbing soup ingredients
    primaryContainers = page_soup.findAll("tr", {"class" : "gridrow"})
    partnerContainters = page_soup.findAll("tr", {"class" : "gridrow_alternate"})

    for primaryContainer in primaryContainers:
