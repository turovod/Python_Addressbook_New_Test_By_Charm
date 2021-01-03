from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            # launch from IDE
            # self.driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")
            # launch from console
            self.driver = webdriver.Firefox(executable_path=self.adapted_url_to_webdriver("Drivers\geckodriver.exe"))
        elif browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=self.adapted_url_to_webdriver("Drivers\chromedriver.exe"))
        elif browser == "edge":
            self.driver = webdriver.Edge(executable_path=self.adapted_url_to_webdriver("Drivers\msedgedriver.exe"))
        else:
            raise ValueError(f"Unrecognised browser {browser}")
        # self.driver.implicitly_wait(1) # waiting in seconds
        # self.base_url = "http://localhost/addressbook/"
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def adapted_url_to_webdriver(self, local_driver_url):
        wd_url = __file__
        wd_url = str(wd_url).strip("fixture\\application.py")
        wd_url = "\\".join([wd_url, local_driver_url])
        return wd_url