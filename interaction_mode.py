from selenium import webdriver
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
    


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
    options.add_argument('--headless')
    choice=input('If you want to specify the chrome driver (binary) path (enter \'y\'). Else to let the code download the driver and detect the default binary path (enter \'n\'): ')
    while choice != 'y' and choice !='n':
        choice=input('Invalid choice! Enter \'y\' to specify paths, and \'n\ not to: ')
    if choice=='n':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    else:
        path=input('chrome path: ') #usr/bin/google-chrome-stable
        driver = webdriver.Chrome(options=options) 
        return driver
