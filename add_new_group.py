# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="aaa", header="bbb", footer="ccc"))
    app.logout()


