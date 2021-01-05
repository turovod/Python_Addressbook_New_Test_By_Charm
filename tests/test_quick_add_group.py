
def test_add_new_group(app, db):
    group = app.group.get_group_from_json()
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    _id = 0
    for i in new_groups:
        if int(i.id) > _id:
            _id = int(i.id)
    group.id = str(_id)
    old_groups.insert(0, group)
    assert sorted(old_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda  group: group.id), f"old_groups {old_groups} == new_groups {new_groups}"

