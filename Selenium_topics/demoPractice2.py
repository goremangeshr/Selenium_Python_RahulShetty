# Validate Total After Discount amount < Total Amount after apply code
import time

from requests.utils import set_environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()             # Open the browser
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for i in results:
    i.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

################## Sum Validation ##############################################
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for i in prices:
    sum = sum + int(i.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount


driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# ++++++++++++++ Compare total amount and amount after discount ++++++++++++++++++++++

discountAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discountAmt
