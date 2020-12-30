
def test_add_new_group(app):
    group = app.group.get_group_from_json()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()  # faster
