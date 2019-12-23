# -*- coding: utf-8 -*-
from operator import index

import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstName", middlename="middleName", lastname="lastName", nickname="nickName",
                       title="titleTest", company="companyTest",
                               address="addressTest", home="homeTest", mobile="mobileTest", work="workTest", fax="faxTest", email="emailTest", email2="emailTest2",
                               email3="emailTest3", homepage="homePage", bday="12", bmonth="June", byear="1995", aday="15", amonth="October", ayear="2010", address2="secondaryAddress",
                               phone2="secondaryHome", notes="notesTest")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    for i in old_contacts:
        old_contacts.append(contact)
        assert old_contacts[i] == new_contacts[i]


