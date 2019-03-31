from selenium import webdriver
import  pytest
from Pages.register import register_user
from Pages.signin import signin
from Pages.flightfinder import flightfinder
from Pages.selectflight import selectflight
from Pages.bookflight import bookflight
from Pages.flightconfirmation import flightconfirmation

@pytest.mark.usefixtures("test_setup")
class Test_mercurydemo:
    def test_register(self):
        driver = self.driver
        ur = register_user(driver)
        ur.click_on_register()
        ur.enter_fn()
        ur.enter_ln()
        ur.enter_ph_no()
        ur.enter_uname()
        ur.enter_local_address()
        ur.enter_local_city()
        ur.enter_local_state()
        ur.enter_local_country()
        ur.enter_local_pcode()
        ur.enter_user_name_red()
        ur.enter_pass()
        ur.enter_conf_pass()
        ur.click_submit()


    def test_login(self):
        driver = self.driver
        li = signin(driver)
        li.click_sign_in()
        li.enter_uname()
        li.enter_pwd()
        li.click_login()


    def test_find_flights(self):
        driver = self.driver
        ff = flightfinder(driver)
        ff.click_oneway()
        ff.select_passengers()
        ff.select_date()
        ff.service_class()
        ff.click_airline()
        ff.click_continue()

    def test_select_flight(self):
        driver = self.driver
        sf = selectflight(driver)
        sf.click_depart1()
        sf.click_back1()
        sf.click_next1()

    def test_book_flight(self):
        driver = self.driver
        bf = bookflight(driver)
        bf.enter_fname()
        bf.enter_lname()
        bf.select_card()
        bf.select_card_no()
        bf.travel_tt()
        bf.book_flight()

    def test_logout(self):
        driver = self.driver
        so = flightconfirmation(driver)
        so.click_btf()
        so.click_signoff()










