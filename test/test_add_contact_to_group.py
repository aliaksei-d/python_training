from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_firstname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    random_group = random.choice(old_groups)
    random_contact = random.choice(old_contacts)
    group_id = int(random_group.id)
    contact_id = int(random_contact.id)
    old_contacts_from_group = db.get_contacts_for_selected_group(group_id)
    app.add_contact_to_group(contact_id, group_id)
    new_contacts_from_group = db.get_contacts_for_selected_group(group_id)
    old_contacts_from_group.append(random_contact)
    assert sorted(old_contacts_from_group, key=Contact.id_or_max) == sorted(new_contacts_from_group, key=Contact.id_or_max)