import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()             # Open the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

############################# Check boxes  ##################################################33
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#
# print(len(checkboxes))
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         print(checkbox.is_selected())
#         break


############################ Radio Button  ###################################################
radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio[2].click()
assert radio[2].is_selected()
# print(len(radio))

# for radio in radio:
#     if radio.get_attribute("value") == "option3":
#         radio.click()
#         print(radio.is_selected())
#         break

################################# is_displayed ##################################################
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
