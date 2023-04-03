import time
import datetime
from datetime import datetime
from selenium.webdriver import Keys
from BasePage import BasePage
from selenium.webdriver.common.by import By
from Locators import osagoLocators



class PageObject(BasePage):

    # Нажатине на кнопку
    def press_button(self, text):
        button = self.find_presence_elements(locator=(By.XPATH, osagoLocators.variable_click(text)))
        button[0].click()

    # Ввод в поле значения
    def input_field_click(self, name, text):
        entry_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.input_field(name)))
        entry_field.click()
        entry_field.send_keys(text)

    # Ввод в поле значения, потом нажать enter
    def input_field_pressEnter(self, name, text):
        entry_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.input_field(name)))
        entry_field.click()
        entry_field.clear()
        entry_field.send_keys(text)
        time.sleep(1)
        entry_field.send_keys(Keys.ENTER)

    # Ввод в поле значения, где есть @class 'select'
    def input_select_click(self, name, text):
        entry_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.select_field(name)))
        entry_field.click()
        entry_field.send_keys(text)

    # Ввод в поле значения, где есть @class 'select', потом нажать enter
    def input_select_pressEnter(self, name, text):
        entry_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.select_field(name)))
        entry_field.click()
        entry_field.clear()
        entry_field.send_keys(text)
        time.sleep(1)
        entry_field.send_keys(Keys.ENTER)

    # Выбор из выпадающего списка
    def input_from_selection(self, name, text):
        entry_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.select_field(name)))
        entry_field.click()
        time.sleep(1)
        selection_value = self.find_presence_element(locator=(By.XPATH, f"//li[text() = '{text}']"))
        selection_value.click()

    # Активировать переключатель
    def switch_press(self, text):
        switch_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.select_switcher(text)))
        time.sleep(1)
        switch_field.click()

    # Получения значения из поля и его сравнение
    def value_field(self, name, text):
        value_type_field = self.find_presence_element(locator=(By.XPATH, osagoLocators.input_field(name)))
        value_type = value_type_field.get_attribute('value')
        assert value_type == text

    # Получения значения из полей даты начала действия и конца действия договора
    def compare_date(self, date_1, date_2):
        date_format = "%d.%m.%Y"
        value_type_field_1 = self.find_presence_element(locator=(By.XPATH, osagoLocators.input_field(date_1)))
        value_type_1 = value_type_field_1.get_attribute('value')
        value_type_1 = datetime.strptime(value_type_1, date_format)
        value_type_field_2 = self.find_presence_element(locator=(By.XPATH, osagoLocators.input_field(date_2)))
        value_type_2 = value_type_field_2.get_attribute('value')
        value_type_2 = datetime.strptime(value_type_2, date_format)
        delta = value_type_2 - value_type_1
        print(delta)


