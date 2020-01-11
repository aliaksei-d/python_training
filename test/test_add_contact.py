# -*- coding: utf-8 -*-
from operator import index

import pytest
from model.contact import Contact
from fixture.application import Application
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                       title="", company="", address="", homephone="",
                      mobilephone="", workphone="",
                      fax="", email="", email2="", email3="",
                      homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
                      ayear="", address2="", secondaryphone="", notes="")] + \
           [Contact(firstname=random_string("firstname", 20), middlename="middleName", lastname=random_string(
               "lastname", 20), nickname="nickName",
            title="titleTest", company="companyTest", address="addressTest", homephone="homephone123",
            mobilephone="+456", workphone="+789",
            fax="fax123", email="email1", email2="email2", email3="email3",
            homepage="homePage", bday="12", bmonth="June", byear="1995", aday="15", amonth="October",
            ayear="2010", address2="secondaryAddress", secondaryphone="secondary1234", notes="notesTest")
            for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(y) for y in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

