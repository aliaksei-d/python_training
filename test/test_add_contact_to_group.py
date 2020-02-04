from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups_list = db.get_group_list()
    random_group = random.choice(groups_list)
    group_id = int(random_group.id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    if len(db.get_contacts_in_group(Group(id="%s" % group_id))) == 0:
        app.contact.create(Contact(firstname="test_firstname"))
    contacts_list = db.get_contacts_not_in_group(Group(id="%s" % group_id))
    random_contact = random.choice(contacts_list)
    contact_id = int(random_contact.id)
    app.contact.add_contact_to_group(contact_id, group_id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id="%s" % group_id))
    old_contacts_in_group.append(random_contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)