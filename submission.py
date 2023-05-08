from selenium import webdriver
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import time
import sys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def read_arguments():
    global user,password,driver
    if len(sys.argv) == 1:
        print('no arguments passed!')
        sys.exit(1)
    elif len(sys.argv)==3: 
        user=sys.argv[1]
        password=sys.argv[2]
        driver=no_interaction(user,password)
    elif sys.argv[1]=='-i' and len(sys.argv)==4:
        browser_choice=input('Use chrome or microsoft edge (Enter c or e): ')
        if browser_choice != 'c' and choice !='e':
            print('Invalid choice for browser: ')
            sys.exit(1)
        if browser_choice=='e':
            driver_path=input('Enter driver path: ')
            binary_path=input('Enter browser path: ')
            driver=interaction_e(driver_path,browser_path)
        else:
            user=sys.argv[2]
            password=sys.argv[3]
            driver=interaction_c()
    else:
        print('arguments missing or in wrong order!')
        sys.exit(1)
    

def no_interaction(user,password):
    # creating a new Edge Driver service object
    edge_service = Service(EdgeChromiumDriverManager().install())
    # setting options through Options object
    options = EdgeOptions()
    options.headless=True  #headless mode, browser hidden
    options.use_chromium = True
    # create a new Edge WebDriver instance
    driver = webdriver.Edge(service=edge_service,options=options)
    return driver



def interaction_e(path1,path2):
    # creating a new Edge Driver service object
    edge_service = Service(path1)
    # setting options through Options object
    options = EdgeOptions()
    options.binary_location = path2
    options.headless=True
    options.use_chromium = True
    # create a new Edge WebDriver instance
    driver = webdriver.Edge(service=edge_service,options=options)
    return driver
    
def interaction_c():
    options = Options()
    #options.add_argument('--headless')
    choice=input('Do you want to specify the chrome driver and binary path or let it download the driver and detect the default binary path (Enter y to specify paths or n): ')
    if choice != 'y' and choice !='n':
        print('Invalid choice!')
        sys.exit(1)
    if choice=='n':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    else:
        path1=input('chrome path: ')
        path2=input('driver path: ')
        options.binary_location=path1
        driver = webdriver.Chrome(service=Service(path2), options=options)
        return driver


read_arguments()

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
    wait = WebDriverWait(driver, 3)


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


#Write data into csv file
i=0
with open('output.csv','w') as o:
    for x in range(22):
        o.write(col_names[x]+',')
    o.write(col_names[22]+'\n')
    
    while i < len(vals):
        for x in range(22):
            o.write(vals[i]+',')
            i+=1
        o.write(vals[i]+'\n')  
        i+=1  

# Mutate data
with open ('output.csv','r') as data, open ('mutated_data.csv','w') as results:
    cols = data.readline().strip().split(',')
    cols[0]='Availibility'
    cols[2]='Subject'
    cols[3]='Course Number'
    cols[4]='Section'
    cols[5]='Campus'
    cols[6]='Credits'
    cols[7]='Course Title'
    cols[10]='Capacity'
    cols[11]='Registered Seats'
    cols[12]='Remaining Seats'
    
    results.write(','.join(cols)+'\n')
    l1=data.readline().strip().split(',')
    l2=data.readline().strip().split(',')
    print(l2[1])
    while len(l1) > 1 and len(l2) > 1:
        if l2[1] == ' ':
            days1=l1[8]
            l1[8]+=f" / {l2[8]}"
            l1[9]+=f" ({days1}) / {l2[9]} ({l2[8]})"
            l1[19]+=f" ({days1}) | {l2[19]} ({l2[8]})" 
            l1[20]+=f" ({days1}) / {l2[20]} ({l2[8]})"
            l1[21]+=f" ({days1}) / {l2[21]} ({l2[8]})" 
            print(l1)
            results.write(','.join(l1)+'\n')
            l1=data.readline().strip().split(',')
        else:
            results.write(','.join(l1)+'\n')  
            l1=l2
        l2=data.readline().strip().split(',')

    if l1[1] != ' ':
        results.write(','.join(l1))
                    

#Close page
driver.quit()

