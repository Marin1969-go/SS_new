from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestNew(unittest.TestCase):
    def test_1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input:required.first")
        input1.send_keys("Marin")
        input2 = browser.find_element(By.CSS_SELECTOR, "input:required.second")
        input2.send_keys("Morr")
        input3 = browser.find_element(By.CSS_SELECTOR, "input:required.third")
        input3.send_keys("morr@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "Registration is failed")

    def test_2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']//following-sibling::input")
        input1.send_keys("Marin")
        input2 = browser.find_element(By.CSS_SELECTOR, "input:required.second")
        input2.send_keys("Morr")
        input3 = browser.find_element(By.CSS_SELECTOR, "input:required.third")
        input3.send_keys("morr@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration is failed")



if __name__ == "__main__":
    pytest.main()