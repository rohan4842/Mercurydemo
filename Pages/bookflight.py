from selenium.webdriver.support.ui import Select
from Testdata import constant as dataval
class bookflight:
    def __init__(self,driver):
        self.driver = driver
        self.fname = "//input[@name='passFirst0']"
        self.lname = "//input[@name='passLast0']"
        self.card_type = "//select[@name='creditCard']"
        self.card_no = "//input[@name='creditnumber']"
        self.tt_travel = "//tr[14]//td[2]//input[1]"
        self.buy_flight = "//input[@name='buyFlights']"

    def enter_fname(self):
        self.driver.find_element_by_xpath(self.fname).send_keys(dataval.BF_FIRSTNAME)
    def enter_lname(self):
        self.driver.find_element_by_xpath(self.lname).send_keys(dataval.BF_LASTNAME)
    def select_card(self):
        card = self.driver.find_element_by_xpath(self.card_type)
        select = Select(card)
        select.select_by_visible_text("MasterCard")
    def select_card_no(self):
        self.driver.find_element_by_xpath(self.card_no).send_keys(dataval.BF_cardno)
    def travel_tt(self):
        self.driver.find_element_by_xpath(self.tt_travel).click()
    def book_flight(self):
        self.driver.find_element_by_xpath(self.buy_flight).click()