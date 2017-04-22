# Title: webscraping_tool_auinvolve.py
# Description: Designed specifically to scrape roster from auinvolve
# Author: Jarrett Tang
# Email: jkt0011@auburn.edu
# !/usr/bin/python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# login function here

# finding max cooking time for soup
def paginationLimit(page_check):
    paginationContainer = page_check.findAll("div", {"class" : "pagination"})
    str_temp = paginationContainer[0].a.next_sibling.next_sibling['href']
    page_number_location = len(str_temp) - 1
    ret_val = str_temp[page_number_location]
    return ret_val
# if there is time add in both different options
# def rosterExtraction1(main_soup):

def fixClassNames(my_soup):
    temp_containers = my_soup.findAll("tr", {"class" : "gridrow_alternate"})
    for temp_container in temp_containers:
        temp_container['class'] = 'gridrow'

my_url = "https://auburn.collegiatelink.net/organization/ewb/roster/members"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# setting up soup recipe
main_soup = soup(page_html, "html.parser")

# required ingredients
MAX_PAGE = paginationLimit(main_soup)
MAIN_URL = 'https://auburn.collegiatelink.net'
PARTNER_URL = '/organization/ewb/roster/members?Direction=Ascending&page='

# file write setup
# filename = "auinvolve_roster_extraction.csv"
# f = open(filename, 'w')
# headers = "First Name,Last Name,Member Since"
# f.write(headers)

# main loop
print("Max number of pages: " + MAX_PAGE)
print("Game time...")
for page_index in range(1, int(MAX_PAGE) + 1):

    # redirects url to roster only section for extraction
    # flips the pages for roster extraction
    my_url = MAIN_URL + PARTNER_URL + str(page_index)

    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # setting up soup recipe
    main_soup = soup(page_html, "html.parser")

    # makes life easier
    fixClassNames(main_soup)

    # grabbing soup ingredients
    name_containers = main_soup.findAll("tr", {"class" : "gridrow"})

    # begin souping.
    # setup specifically for a not logged in system.
    # idea: use concatenation to modify these data grabbing lines
    # instead of writing more than one function.
    for name_container in name_containers:
        first_name = name_container.td.next_sibling.string
        last_name = name_container.td.next_sibling.next_sibling.string
        date_joined = name_container.td.next_sibling.next_sibling.next_sibling.string

        print("first name: " + first_name)
        print("last name: " + last_name)
        print("Member Since: " + date_joined)
