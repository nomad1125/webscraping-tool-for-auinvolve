# Title: webscraping_tool_auinvolve.py
# Description: Designed specifically to scrape roster from auinvolve
# Author: Jarrett Tang
# Email: jkt0011@auburn.edu
# !/usr/bin/python3.6

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# finding max cooking time for soup
def paginationLimit(page_check):
    paginationContainer = page_check.findAll("div", {"class" : "pagination"})
    str_temp = paginationContainer[0].a.next_sibling.next_sibling['href']
    page_number_location = len(str_temp) - 1
    ret_val = str_temp[page_number_location]
    return ret_val

#roster extraction function if NOT logged into AU Involve
def rosterExtractionNotLoggedIn(name_container):
    first_name = name_container.td.next_sibling.string
    last_name = name_container.td.next_sibling.next_sibling.string
    date_joined = name_container.td.next_sibling.next_sibling.next_sibling.string

    print("First Name: " + first_name)
    print("Last Name: " + last_name)
    print("Member Since: " + date_joined + "\n")

    ret_val = first_name + "," + last_name + "," + date_joined + "\n"
    return ret_val

# roster extraction if logged into Auinvolve.
# still needs to be adjust for the for loop.
def rosterExtractionLoggedIn(name_container):
    more_info = name_container.td.next_sibling.next_sibling.div.a['href']
    first_name = name_container.td.next_sibling.next_sibling.div.string
    last_name = name_container.td.next_sibling.next_sibling.next_sibling.next_sibling.div.string
    date_joined = name_container.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string

    uClient = uReq(MAIN_URL + more_info)
    temp_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    temp_containers = temp_soup.findAll("div", {"class" : "userCard-info vcard"})
    email_address = temp_containers[0].div.div.a.span.next_sibling.strip()

    print("First Name: " + first_name)
    print("Last Name: " + last_name)
    print("Member Since: " + date_joined)
    print("Email Address " + email_address + "\n")

    ret_val = first_name + "," + last_name + "," + date_joined + "," + email_address + "\n"
    return ret_val

# this function saves lives by making all the search tags
# the same making life easier.
def fixClassNames(my_soup):
    temp_containers = my_soup.findAll("tr", {"class" : "gridrow_alternate"})
    for temp_container in temp_containers:
        temp_container['class'] = 'gridrow'

# login function here
isLoggedIn = False

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
filename = "auinvolve_roster_extraction.csv"
f = open(filename, 'w')
if isLoggedIn:
    header_extension = ",Email"

else:
    header_extension = ""
    print("WARNING: Not logged into AU Involve\n" +
          "\tSome names may be missing.\n")

headers = "First Name,Last Name,Member Since" + header_extension +"\n"
f.write(headers)

# main loop
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
    for name_container in name_containers:
        if isLoggedIn:
            print("logged in version missing...")

        else:
            write_out = rosterExtractionNotLoggedIn(name_container)

        f.write(write_out)

f.close()
