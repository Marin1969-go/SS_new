import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class UniqSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def form_reg(self, link):
        driver = self.driver
        driver.get(link)
        fn = driver.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
        fn.send_keys('Mar')
        ln = driver.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
        ln.send_keys('Morr')
        em = driver.find_element(By.XPATH, '//label[text()="Email*"]/following-sibling::input')
        em.send_keys('morr@yamdex.ru')
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        return driver.find_element(By.CSS_SELECTOR, 'h1').text

    def test_url1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual('Congratulations! You have successfully registered!', self.form_reg(link),"whoops")
    def test_url2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual('Congratulations! You have successfully registered!', self.form_reg(link),"whoops2")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()