from model.group import Group
import random


def test_modify_group_name(app, db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    modify_group = random.choice(old_groups)
    group = Group(name="New Group", id=modify_group.id)
    app.group.modify_group_by_id(modify_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[old_groups.index(modify_group)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app, db):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test"))
#     old_groups = db.get_group_list()
#     group = random.choice(old_groups)
#     group = Group(name="New Group")
#     app.group.modify_group_by_id(group.id, group)
#     new_groups = db.get_group_list()
#     assert len(old_groups) == app.group.count()
#     old_groups.modify(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)