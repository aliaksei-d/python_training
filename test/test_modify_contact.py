from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.modify_first_contact(Contact(firstname="New first name"))
#    app.return_to_home_page()


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.modify_first_contact(Contact(lastname="New last name"))
#   app.return_to_home_page()