from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

constant = [
    Contact(firstname="f1", middlename="m1", lastname="l1", nickname="n1",
            title="t1", company="c1", address="a1", homephone="h1",
            mobilephone="m1", workphone="w1",
            fax="f1", email="e1", email2="e2", email3="e3",
            homepage="ho1", bday="", bmonth="-", byear="", aday="", amonth="-",
            ayear="", address2="a2", secondaryphone="sec1", notes="n1")
]


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