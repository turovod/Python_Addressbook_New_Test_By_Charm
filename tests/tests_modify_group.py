from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="mod_name"))
    app.group.modify(Group(name="modify_aaa"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="mod_header"))
    app.group.modify(Group(header="modify_bbb"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="mod_footer"))
    app.group.modify(Group(footer="modify_ccc"))
