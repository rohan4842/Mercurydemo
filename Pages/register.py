from selenium.webdriver.support.ui import Select
from Testdata import constant as dataval
class register_user:
    def __init__(self,driver):
        self.driver = driver
        self.register_link = "//a[contains(text(),'REGISTER')]"
        self.first_name = "//input[@name='firstName']"
        self.last_name = "//input[@name='lastName']"
        self.phone_no = "//input[@name='phone']"
        self.user_name = "//input[@id='userName']"
        self.address = "//input[@name='address1']"
        self.city = "//input[@name='city']"
        self.state = "//input[@name='state']"
        self.postal_code = "//input[@name='postalCode']"
        self.country = "//select[@name='country']"
        self.uname_red = "//input[@id='email']"
        self.password = "//input[@name='password']"
        self.confirm_password = "//input[@name='confirmPassword']"
        self.submit = "//input[@name='register']"

    def click_on_register(self):
        self.driver.find_element_by_xpath(self.register_link).click()
    def enter_fn(self):
        self.driver.find_element_by_xpath(self.first_name).send_keys(dataval.FIRST_NAME)
    def enter_ln(self):
        self.driver.find_element_by_xpath(self.last_name).send_keys(dataval.LAST_NAME)
    def enter_ph_no(self):
        self.driver.find_element_by_xpath(self.phone_no).send_keys(dataval.PHONE_NO)
    def enter_uname(self):
        self.driver.find_element_by_xpath(self.user_name).send_keys(dataval.USERNAME)
    def enter_local_address(self):
        self.driver.find_element_by_xpath(self.address).send_keys(dataval.ADDRESS)
    def enter_local_city(self):
        self.driver.find_element_by_xpath(self.city).send_keys(dataval.CITY)
    def enter_local_state(self):
        self.driver.find_element_by_xpath(self.state).send_keys(dataval.STATE)
    def enter_local_pcode(self):
        self.driver.find_element_by_xpath(self.postal_code).send_keys(dataval.POSTAL_CODE)
    def enter_local_country(self):
        select_country = self.driver.find_element_by_xpath(self.country)
        select = Select(select_country)
        select.select_by_value("92")
    def enter_user_name_red(self):
        self.driver.find_element_by_xpath(self.uname_red).send_keys(dataval.EMAIL)
    def enter_pass(self):
        self.driver.find_element_by_xpath(self.password).send_keys(dataval.PASSWORD)
    def enter_conf_pass(self):
        self.driver.find_element_by_xpath(self.confirm_password).send_keys(dataval.CONFIRM_PASS)
    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit).click()