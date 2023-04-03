from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def find_visible_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_visible_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def find_presence_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_presence_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))