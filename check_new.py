from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestNew(unittest.TestCase):
    def setUp(self):

        self.browser = webdriver.Chrome()

    def registration_full(self,link):
        self.browser.get(link)
        browser = self.browser
        # заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        input1.send_keys("Marin")
        input2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        input2.send_keys("Morr")
        input3 = browser.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        input3.send_keys("morr@yandex.ru")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt= WebDriverWait(self.browser, 5).until(
           EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        return welcome_text

    def test_url1(self):
            link = 'http://suninjuly.github.io/registration1.html'
            self.assertEqual('Congratulations! You have successfully registered!', self.registration_full(link), "whoops...Registration is failed")

    def test_url2(self):
           link = 'http://suninjuly.github.io/registration2.html'
           self.assertEqual('Congratulations! You have successfully registered!', self.registration_full(link), "whoops2...Registration is failed")

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()








