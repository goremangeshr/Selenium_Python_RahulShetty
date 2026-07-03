import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()             # Open the browser
# driver.get("https://rahulshettyacademy.com/client")     # get the website
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()       # find locator by Link_Text
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")        # find locator by xpath parent to child
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("password")   # find locator by css parent to child
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys("password")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()   #find locator using xpath and text()




