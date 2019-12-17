from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New first name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New last name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
