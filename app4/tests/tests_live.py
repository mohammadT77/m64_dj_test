from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class RegistrationLiveTest(StaticLiveServerTestCase):
    selenium: WebDriver

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # cls.selenium.quit()
        super().tearDownClass()

    def test_(self):
        self.selenium.get(f"{self.live_server_url}/auth/register")
        username_elem = self.selenium.find_element('name', 'username')
        username_elem.send_keys('Akbar')

        password_elem = self.selenium.find_element('name', 'password')
        password_elem.send_keys('akbar')

        firstname_elem = self.selenium.find_element('name', 'first_name')
        firstname_elem.send_keys('Akbar')

        lastname_elem = self.selenium.find_element('name', 'last_name')
        lastname_elem.send_keys('Babaii')

        submit_elem = self.selenium.find_element('css selector', 'input[type=submit]')
        submit_elem.click()

        self.selenium.get(f"{self.live_server_url}/auth/login")
        username_elem = self.selenium.find_element('name', 'username')
        username_elem.send_keys('Akbar')

        password_elem = self.selenium.find_element('name', 'password')
        password_elem.send_keys('akbar')

        submit_elem = self.selenium.find_element('css selector', 'input[type=submit]')
        submit_elem.click()






