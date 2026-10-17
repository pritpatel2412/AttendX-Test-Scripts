import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://the-internet.herokuapp.com/login"


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()      # Selenium 4 auto-manages the driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def _login(self, username, password):
        d = self.driver
        d.get(LOGIN_URL)
        d.find_element(By.ID, "username").send_keys(username)
        d.find_element(By.ID, "password").send_keys(password)
        d.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def _flash_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text

    def test_valid_login(self):
        """TC-L01: valid credentials log the user in."""
        self._login("tomsmith", "SuperSecretPassword!")
        self.assertIn("You logged into a secure area!", self._flash_message())

    def test_invalid_password(self):
        """TC-L02: wrong password shows an error."""
        self._login("tomsmith", "wrongpassword")
        self.assertIn("Your password is invalid!", self._flash_message())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
```