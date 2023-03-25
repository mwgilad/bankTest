import pytest

from finalFunctions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestBank:
    # set driver as variable
    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    # set url as variable
    @pytest.fixture()
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    # test that the url directs to and opens the website (most basic test)
    def test_sanity(self, driver, url):
        expected = url
        actual = open_webpage(driver, expected)
        assert expected == actual

    # test that the process of adding a new customer does not continue without entering a first name
    @pytest.mark.parametrize('fname, lname, zipcode', [('', 'Humphrey', '10128')])
    def test_newCustomer_N(self, driver, url, fname, lname, zipcode):
        open_webpage(driver, url)
        actual = add_new_customer(driver, fname, lname, zipcode)
        expected = False
        assert actual == expected

    #test that new customer is added and search for the new customer's name
    @pytest.mark.parametrize('fname, lname, zipcode', [('Dan', 'Humphrey', '10128')])
    def test_addNewCustomer(self, driver, url, fname, lname, zipcode):
        open_webpage(driver, url)
        add_new_customer(driver, fname, lname, zipcode)
        actual = find_customer(driver, fname, lname)
        expected = True
        assert actual == expected

    # test deposit and withdraw then check that the balance is accurate
    @pytest.mark.parametrize('deposit_amount, withdraw_amount', [(1000, 250)])
    def test_deposit_and_withdraw_neville(self,driver,url,deposit_amount,withdraw_amount):
        open_webpage(driver, url)
        log_in_neville(driver)
        if deposit_neville(driver, deposit_amount) == True and withdraw_neville(driver, withdraw_amount) == True:
            actual = balance_neville(driver)
        else:
            actual = False
        expected = '750'
        assert actual == expected


