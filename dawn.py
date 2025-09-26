import os
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR, "input:required[name=firstname]")
    input1.send_keys("Marin")
    input2= browser.find_element(By.CSS_SELECTOR, "input:required[name=lastname]")
    input2.send_keys("Morr")
    input3 = browser.find_element(By.CSS_SELECTOR, "input:required[name=email]")
    input3.send_keys("morr@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname('dawnload_file'))
    print(current_dir)
    file_name = "file11.txt"
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    button= browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()