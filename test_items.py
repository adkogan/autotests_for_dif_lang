import time
import unittest

def test_find_add_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    # browser.find_element_by_class_name('btn-add-to-basket')
    assert len(browser.find_elements_by_class_name('btn-add-to-basket'))==1, 'The "add to basket" button does not exist!'
