from model.contact import Contact
import random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_firstname"))
    old_contacts = db.get_contact_list()
    modify_contact = random.choice(old_contacts)
    contact = Contact(firstname="New first name", lastname="New last name", id=modify_contact.id)
    app.contact.modify_contact_by_id(modify_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[old_contacts.index(modify_contact)] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test_contact"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(lastname="New last name")
#     contact.id = old_contacts[0].id
#     app.contact.modify_first_contact(contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)