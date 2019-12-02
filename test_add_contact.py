# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import pytest
from contact import Contact
from application2 import Application2


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application2()

    def test_add_contact(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="firstName", middlename="middleName", lastname="lastName", nickname="nickName", title="titleTest", company="companyTest",
                            address="addressTest", home="homeTest", mobile="mobileTest", work="workTest", fax="faxTest", email="emailTest", email2="emailTest2",
                            email3="emailTest3", homepage="homePage", bday="12", bmonth="June", byear="1995", aday="15", amonth="October", ayear="2010", address2="secondaryAddress",
                            phone2="secondaryHome", notes="notesTest"))
        self.app.return_to_home_page()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

