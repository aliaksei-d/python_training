from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    random_group = random.choice(groups_list)
    group_id = int(random_group.id)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_firstname"))
        new_contact = db.get_contact_list()[0]
        app.contact.add_contact_to_group(new_contact.id, group_id)
    elif len(db.get_contacts_in_group(Group(id="%s" % group_id))) == 0:
        contacts_list_not_in_group = db.get_contacts_not_in_group(Group(id="%s" % group_id))
        random_contact = random.choice(contacts_list_not_in_group)
        app.contact.add_contact_to_group(random_contact.id, group_id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    old_contacts_list = db.get_contact_list()
    random_contact = random.choice(old_contacts_in_group)
    contact_id = int(random_contact.id)
    app.contact.delete_contact_from_group(contact_id, group_id)
    new_contacts_list = db.get_contact_list()
    new_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    old_contacts_in_group.remove(random_contact)
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)