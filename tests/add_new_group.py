# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="aaa", header="bbb", footer="ccc"))
    app.session.logout()
