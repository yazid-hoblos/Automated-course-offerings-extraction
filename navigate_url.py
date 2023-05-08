from selenium import webdriver   
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

import sys 

def navigate_url(user,password,driver):
    # use the driver to navigate to a website
    url='https://myportal.lau.edu.lb'
    driver.get(url)

    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    username_field.send_keys(user)
    password_field.send_keys(password)

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    if not 'studentPortal' in driver.current_url:
        print("login failed! Recheck your credentials.")
        sys.exit(1)
    else:
        print("Successful Login!")


    # find all the <a> elements that have the word "courses" in their href attribute
    elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'courses')]")
    # extract the href attribute from each link
    hrefs = [e.get_attribute("href") for e in elements]
    driver.get(hrefs[0])


    # find all the <a> elements that have the word "ban" in their href attribute
    elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'ban')]")
    # extract the href attribute from each link
    hrefs2 = [e.get_attribute("href") for e in elements]
    # navigate to registration menu
    for x in hrefs2:
        if "name=bmenu.P_RegMnu" in x:
            driver.get(x)


    # find all the <a> elements that have the word "prod" in their href attribute
    elements = driver.find_elements(By.XPATH, "//a[contains(@href,'prod')]")
    hrefs3 = [e.get_attribute("href") for e in elements]

    # navigate to courses search page
    for x in hrefs3:
        if "search" in x:
            driver.get(x)

    
    # locate the dropdown element
    dropdown = driver.find_element(By.ID, 'term_input_id')
    # create a Select object for the dropdown element
    select = Select(dropdown)
    # select the option by value
    select.select_by_value('202410') #for Fall 2023

    button = driver.find_element(By.XPATH, "//input[contains(@value,\"Submit\")]")
    button.click()
    
    button = driver.find_element(By.XPATH, "//input[contains(@value,\"Advanced Search\")]")
    button.click()

    dropdown = driver.find_element(By.ID, 'camp_id')
    select=Select(dropdown)
    select.select_by_value('2')
    select.deselect_by_value('%')

    dropdown = driver.find_element(By.ID, 'subj_id')
    select=Select(dropdown)
    select.select_by_value('BIF')
    select.select_by_value('CSC')
    select.select_by_value('MTH')

    button = driver.find_element(By.XPATH, "//input[contains(@value,\"Section Search\")]")
    button.click()

    # Extract column names
    cols = driver.find_elements(By.XPATH, "//th[contains(@class, 'ddheader')]") #23 columns
    col_names = [c.text for c in cols]

    # Extract data
    elements = driver.find_elements(By.XPATH, "//td[contains(@class, 'dddefault')]") #23 columns
    vals = [e.text for e in elements]
    return col_names, vals

    driver.quit()