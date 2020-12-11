from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="modify_aaa"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header="modify_bbb"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(footer="modify_ccc"))
    app.session.logout()