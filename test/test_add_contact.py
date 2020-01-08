# -*- coding: utf-8 -*-
from operator import index

import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstName", middlename="middleName", lastname="lastName", nickname="nickName",
                       title="titleTest", company="companyTest", address="addressTest", homephone="homephone123",
                      mobilephone="+456", workphone="+789",
                      fax="fax123", email="email1", email2="email2", email3="email3",
                      homepage="homePage", bday="12", bmonth="June", byear="1995", aday="15", amonth="October",
                      ayear="2010", address2="secondaryAddress", secondaryphone="secondary1234", notes="notesTest")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

