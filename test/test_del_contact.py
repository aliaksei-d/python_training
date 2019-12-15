from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact"))
    app.contact.delete_first_contact()
    app.return_to_home_page()
