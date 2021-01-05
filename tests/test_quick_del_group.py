import random
from model.group import Group


def test_quick_delete_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="del_name"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups



