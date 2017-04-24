# Title: webscraping_login_tool_auinvolve.py
# Description: Prompts the user for the username and password that they desire
#              to log in with.  The program will then log in to AUinvolve.
# Author: David S Stein
# Date: 19 April 2017


import mechanicalsoup

def logIntoAuinvolve(username, password, response_page):

    LOGIN_URL = "https://authenticate.auburn.edu/cas/login?" +
                "service=https%3a%2f%2ffederation.campuslabs.com%2fauth%2fsignin%2f"
    LOGIN_NAME = username
    LOGIN_PASS = password

    browser = mechanicalsoup.Browser()

    login_page = browser.get(LOGIN_URL)

    login_form = login_page.soup.find("div",{"class" : "signin"})

    login_form.find("input", {"id" : "username"})[]
