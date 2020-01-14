from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))