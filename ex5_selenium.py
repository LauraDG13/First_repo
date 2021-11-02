#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:19:49 2019

@author: macbookpro
"""

"""
This script takes the Quarter, Items, Amount and Total Amount columns from the table at
http://testing-ground.scraping.pro/table?products=1&years=1&quarters=4
and write them to a properly formatted CSV file.
Scraping is performed exploiting Selenium library and Chrome browser.

"""

# TO-DO: import python modules used in the script
# csv

import csv

# TO-DO: import python selenium module

from selenium import webdriver


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

target_url = 'http://testing-ground.scraping.pro/table?products=1&years=1&quarters=4'

# TO-DO: create a Chrome instance by means of the webdriver, and open the web page:

print("Open a browser and navigate to {0} ...".format(target_url))

driver = webdriver.Chrome()
driver.get(target_url)

# TO-DO: by means of CSS selectors, select table, thead and tbody elements
# using find_element_by_css_selector(...) method


# TO-DO: open a writable CSV file "table.csv"

with open('table.csv', 'w') as handle:
    file_writer = csv.writer(handle, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # TO-DO: using the table thead element, scan the header and create the proper CSV header

    file_headers= ['quarter', 'product 1', 'items', 'amount', 'total amount' ]
    file_writer.writerow(file_headers)

    # get the table header
    
    

    # TO-DO: write the CSV file header

    # TO-DO: using the table thead element, scan the table rows, get the data and create the CSV body

    # get the table body
    # scan the table body rows

        # scan the row cells
        # check if the cell has an attribute 'colspan', and if it does discard the entire row

        # TO-DO: write the row to the CSV file, if needed


# TO-DO: quit the Chrome instance
