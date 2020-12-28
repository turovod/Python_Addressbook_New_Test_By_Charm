from model.group import Group


def test_add_new_group1(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()  # faster
    new_groups = app.group.get_group_list()
    _id = 0
    for i in new_groups:
        if int(i.id) > _id:
            _id = int(i.id)
    group.id = str(_id)
    old_groups.insert(0, group)
    assert sorted(old_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id), f"old_groups {old_groups} == new_groups {new_groups}"