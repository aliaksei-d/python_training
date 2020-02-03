import re
from model.contact import Contact


def test_data_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    while index <= int(len(contacts_from_home_page)-1):
        contact = contacts_from_db[index]
        assert contacts_from_home_page[index].firstname == contacts_from_db[index].firstname
        assert contacts_from_home_page[index].lastname == contacts_from_db[index].lastname
        assert contacts_from_home_page[index].address == contacts_from_db[index].address
        assert contacts_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact)
        assert contacts_from_home_page[index].all_emails_from_home_page == merge_emails_like_on_home_page(contact)
        index=index+1



def clear(s):
    return re.sub("[() -]", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))