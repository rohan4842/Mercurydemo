from selenium.webdriver.support.ui import Select
from Testdata import constant as dataval
class flightfinder:
    def __init__(self,driver):
        self.driver = driver
        self.one_way = "//input[@value='oneway']"
        self.no_passengers = "//select[@name='passCount']"
        self.date_journey = "//select[@name='fromDay']"
        self.preference = "//input[@value='Business']"
        self.airline = "//select[@name='airline']"
        self.submit_continue = "//input[@name='findFlights']"

    def click_oneway(self):
        self.driver.find_element_by_xpath(self.one_way).click()
    def select_passengers(self):
        passenger = self.driver.find_element_by_xpath(self.no_passengers)
        select = Select(passenger)
    def select_date(self):
        date = self.driver.find_element_by_xpath(self.date_journey)
        select = Select(date)
        select.select_by_index(23)
    def service_class(self):
        self.driver.find_element_by_xpath(self.preference).click()
    def click_airline(self):
        self.driver.find_element_by_xpath(self.airline).click()
    def click_continue(self):
        self.driver.find_element_by_xpath(self.submit_continue).click()
