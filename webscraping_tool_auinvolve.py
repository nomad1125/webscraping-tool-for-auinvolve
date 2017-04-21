# Title: webscraping_tool_auinvolve.py
# Description: Designed specifically to scrape roster from auinvolve
# Author: Jarrett Tang
# Email: jkt0011@auburn.edu
# !/usr/bin/python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# login function here

my_url = "https://auburn.collegiatelink.net/organization/ewb/roster/members"

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

# required ingredients
MAX_PAGE = paginationLimit(page_soup)
MAIN_URL = "https://auburn.collegiatelink.net"
PARTNER_URL = "/organization/ewb/roster/members?Direction=Ascending&amp;page="

# main loop
for page_index in range(1, MAX_PAGE):

    # redirects url to roster only section for extraction
    # flips the pages for roster extraction
    my_url = MAIN_URL + PARTNER_URL + page_index

    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #grabbing soup ingredients
    primaryContainers = page_soup.findAll("tr", {"class" : "gridrow"})
    partnerContainters = page_soup.findAll("tr", {"class" : "gridrow_alternate"})

    for primaryContainer in primaryContainers:
