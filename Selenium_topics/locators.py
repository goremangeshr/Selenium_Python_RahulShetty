import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()             # Open the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")     # Get the URL
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")      # find locator by NAME
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")  # find locator by ID
driver.find_element(By.ID, "exampleCheck1").click()                     # find locator by ID

# Xpath - //tagname[@attribute='value']
# CSS - tagname[attribute='value'] .alert-success
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Mangesh Gore")
# message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text                 # find locator by css
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()           # find locator by css

driver.find_element(By.XPATH,"//input[@type='submit']").click()         # find locator by Xpath
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("12345") # find locator by xpath-index

message = driver.find_element(By.CLASS_NAME, "alert-success").text      # find locator by Class_Name
print(message)

driver.find_element(By.CLASS_NAME, "alert-success").clear()         # .clear will clear the data from selcted locator
assert "Success" in message

############### STATIC DROPDOWN ###########################

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

############### Auto Suggestive Drop Down ############################



