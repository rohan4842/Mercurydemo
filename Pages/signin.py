from Testdata import constant as dataval

class signin:
    def __init__(self,driver):
        self.driver = driver
        self.sign_in = "//a[contains(text(),'sign-in')]"
        self.uname = "//input[@name='userName']"
        self.pwd = "//input[@name='password']"
        self.login = "//input[@value='Login']"

    def click_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in).click()
    def enter_uname(self):
        self.driver.find_element_by_xpath(self.uname).send_keys(dataval.EMAIL)
    def enter_pwd(self):
        self.driver.find_element_by_xpath(self.pwd).send_keys(dataval.PASSWORD)
    def click_login(self):
        self.driver.find_element_by_xpath(self.login).click()