class selectflight:
    def __init__(self,driver):
        self.driver = driver
        self.depart = "//input[@value='Pangea Airlines$362$274$9:17']"
        self.back = "//input[@value='Pangea Airlines$632$282$16:37']"
        self.next = "//input[@name='reserveFlights']"

    def click_depart1(self):
        while True:
            try:
               self.driver.find_element_by_xpath(self.depart).click()
               break
            except:
                print("waiting for element to be clickable")
    def click_back1(self):
        self.driver.find_element_by_xpath(self.back).click()
    def click_next1(self):
        self.driver.find_element_by_xpath(self.next).click()

