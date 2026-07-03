import time
from selenium import webdriver
from selenium.webdriver.common.by import By

################### Implicit Wait #####################################
name = 'Mangesh'
driver = webdriver.Chrome()             # Open the browser
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for i in results:
    i.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("abc")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

