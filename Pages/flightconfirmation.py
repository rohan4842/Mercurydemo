class flightconfirmation:
    def __init__(self,driver):
        self.driver = driver
        self.backtoflight = "//img[@src='/images/forms/backtoflights.gif']"
        self.signoff = "//a[contains(text(),'SIGN-OFF')]"

    def click_btf(self):
            self.driver.find_element_by_xpath(self.backtoflight).click()
    def click_signoff(self):
            self.driver.find_element_by_xpath(self.signoff).click()

