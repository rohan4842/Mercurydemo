from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com/create_account_success.php")
driver.find_element_by_xpath("//a[contains(text(),'sign-in')]").click()
driver.find_element_by_xpath("//input[@name='userName']").send_keys("rohn")
driver.find_element_by_xpath("//input[@name='password']").send_keys("rohn")
driver.find_element_by_xpath("//input[@value='Login']").click()

driver.find_element_by_xpath("//input[@value='oneway']").click()

passenger = driver.find_element_by_xpath("//select[@name='passCount']")
select = Select(passenger)
select.select_by_index(2)

date = driver.find_element_by_xpath("//select[@name='fromDay']")
select = Select(date)
select.select_by_index(23)

driver.find_element_by_xpath("//input[@value='Business']").click()

airline = driver.find_element_by_xpath("//select[@name='airline']")
select = Select(airline)
select.select_by_visible_text("Unified Airlines")

driver.find_element_by_xpath("//input[@name='findFlights']").click()
#
driver.find_element_by_xpath("//input[@value='Unified Airlines$363$281$11:24']").click()
driver.find_element_by_xpath("//input[@value='Blue Skies Airlines$631$273$14:30']").click()
driver.find_element_by_xpath("//input[@name='reserveFlights']").click()
#
driver.find_element_by_xpath("//input[@name='passFirst0']").send_keys("test_name")
driver.find_element_by_xpath("//input[@name='passLast0']").send_keys("test_last")

card = driver.find_element_by_xpath("//select[@name='creditCard']")
select = Select(card)
select.select_by_visible_text("MasterCard")

driver.find_element_by_xpath("//input[@name='creditnumber']").send_keys("4111")

driver.find_element_by_xpath("//tr[14]//td[2]//input[1]").click()
driver.find_element_by_xpath("//input[@name='buyFlights']").click()




#driver.quit()












'''
driver.get("http://newtours.demoaut.com/mercurywelcome.php")
driver.maximize_window()

driver.find_element_by_xpath("//a[contains(text(),'REGISTER')]").click()
driver.find_element_by_xpath("//input[@name='firstName']").send_keys("test_first")
driver.find_element_by_xpath("//input[@name='lastName']").send_keys("test_last")
driver.find_element_by_xpath("//input[@name='phone']").send_keys("1234567890")
driver.find_element_by_xpath("//input[@id='userName']").send_keys("test@test.com")
driver.find_element_by_xpath("//input[@name='address1']").send_keys("test_address")
driver.find_element_by_xpath("//input[@name='city']").send_keys("test_city")
driver.find_element_by_xpath("//input[@name='state']").send_keys("test_state")
driver.find_element_by_xpath("//input[@name='postalCode']").send_keys("50215")

select_country =driver.find_element_by_xpath("//select[@name='country']")
select = Select(select_country)
select.select_by_value("92")

driver.find_element_by_xpath("//input[@id='email']").send_keys("test_un")
driver.find_element_by_xpath("//input[@name='password']").send_keys("test_pwd")
driver.find_element_by_xpath("//input[@name='confirmPassword']").send_keys("test_pwd")
driver.find_element_by_xpath("//input[@name='register']").click()


driver.get("http://newtours.demoaut.com/create_account_success.php")
driver.find_element_by_xpath("//a[contains(text(),'sign-in')]").click()
driver.find_element_by_xpath("//input[@name='userName']").send_keys("test_user")
driver.find_element_by_xpath("//input[@name='password']").send_keys()

#driver.quit()
'''