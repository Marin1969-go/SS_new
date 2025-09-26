from selenium import webdriver
from selenium.webdriver.common.by import By
import math,time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, "input_value").text)
    answer = calc(x)
    print(answer)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
finally:
    time.sleep(5)
    browser.quit()
