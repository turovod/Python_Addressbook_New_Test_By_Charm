# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="aaa", header="bbb", footer="ccc"))
    app.session.logout()


