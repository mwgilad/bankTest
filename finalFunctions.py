from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def get_element(driver, CSS_path):
    return driver.find_element(By.CSS_SELECTOR, CSS_path)



def open_webpage(driver, url):
    driver.get(url)
    time.sleep(2)
    return driver.current_url

def add_new_customer(driver, fname, lname, zipcode):
    try:
        manager_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
        manager_btn.click()
        time.sleep(1)
        add_cus_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
        add_cus_btn.click()
        time.sleep(1)
        firstname = get_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input')
        firstname.send_keys(fname)
        lastname = get_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
        lastname.send_keys(lname)
        zipc = get_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
        zipc.send_keys(zipcode)
        add_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
        add_btn.click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        return True
    except:
        return False


def find_customer(driver, fname):
    customer_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
    customer_btn.click()
    time.sleep(1)
    source = driver.page_source
    if fname in source:
        return True
    else:
        return False


def log_in_neville(driver):
    cust_login_btn = get_element(driver,'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
    cust_login_btn.click()
    time.sleep(1)
    dropdown = get_element(driver,'#userSelect')
    dropdown
    neville = get_element(driver, '#userSelect > option:nth-child(6)')
    neville.click()
    time.sleep(1)
    login_btn = get_element(driver,'body > div > div > div.ng-scope > div > form > button')
    login_btn.click()
    time.sleep(1)

def deposit_neville(driver, amount):
    deposit_menu_btn = get_element(driver,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    deposit_menu_btn.click()
    time.sleep(1)
    amount_input = get_element(driver, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    amount_input.send_keys(amount)
    time.sleep(1)
    deposit_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    deposit_btn.click()
    time.sleep(1)

def withdraw_neville(driver, amount):
    withdraw_menu_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)')
    withdraw_menu_btn.click()
    time.sleep(1)
    amount_input = get_element(driver, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    amount_input.send_keys(amount)
    time.sleep(1)
    withdraw_btn = get_element(driver, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    withdraw_btn.click()
    time.sleep(1)

def balance_neville(driver):
    balance = get_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')
    return balance.text
