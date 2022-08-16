from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "button").click()
confirm = browser.switch_to.alert
confirm.accept()

##browser.switch_to.window(0)
x_elements = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = int(x_elements.text)
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.TAG_NAME, "button").click()
time.sleep(40)
browser.quit()