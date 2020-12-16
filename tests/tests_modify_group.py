from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="mod_name"))

    old_groups = app.group.get_group_list()
    app.group.modify(Group(name="modify_aaa"))
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="mod_header"))

    old_groups = app.group.get_group_list()
    app.group.modify(Group(header="modify_bbb"))
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="mod_footer"))

    old_groups = app.group.get_group_list()
    app.group.modify(Group(footer="modify_ccc"))
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)
