from model.group import Group


def test_modify_group_name(app):
    app.group.modify(Group(name="modify_aaa"))


def test_modify_group_header(app):
    app.group.modify(Group(header="modify_bbb"))


def test_modify_group_footer(app):
    app.group.modify(Group(footer="modify_ccc"))
