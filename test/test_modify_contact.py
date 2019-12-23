from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New first name"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New last name"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()