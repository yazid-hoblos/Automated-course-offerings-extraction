from selenium import webdriver
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager


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