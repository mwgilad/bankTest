import pytest

from finalFunctions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestBank:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    @pytest.fixture()
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def test_sanity(self, driver, url):
        expected = url
        actual = open_webpage(driver, expected)
        assert expected == actual

    @pytest.mark.parametrize('fname, lname, zipcode', [('', 'Humphrey', '10128')])
    def test_newCustomer_N(self, driver, url, fname, lname, zipcode):
        open_webpage(driver, url)
        actual = add_new_customer(driver, fname, lname, zipcode)
        expected = False
        assert actual == expected

    @pytest.mark.parametrize('fname, lname, zipcode', [('Dan', 'Humphrey', '10128')])
    def test_addNewCustomer(self, driver, url, fname, lname, zipcode):
        open_webpage(driver, url)
        add_new_customer(driver, fname, lname, zipcode)
        actual = find_customer(driver, fname)
        expected = True
        assert actual == expected

    @pytest.mark.parametrize('deposit_amount, withdraw_amount', [(1000, 250)])
    def test_deposit_and_withdraw_neville(self,driver,url,deposit_amount,withdraw_amount):
        open_webpage(driver, url)
        log_in_neville(driver)
        deposit_neville(driver, deposit_amount)
        withdraw_neville(driver, withdraw_amount)
        actual = balance_neville(driver)
        expected = '750'
        assert actual == expected






