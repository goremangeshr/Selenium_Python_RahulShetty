import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

# service_obj = Service("C:/Program Files/Google/Chrome/Application/chrome.exe")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()             # Open the browser
driver.get("https://rahulshettyacademy.com")     # Get the URL
driver.maximize_window()                # maximize the window
print(driver.title)                     # get the title of the page
print(driver.current_url)               # get the current url of the page















time.sleep(2)
