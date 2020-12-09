# -*- coding: utf-8 -*-
from group import Group
import unittest
from application import Application


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_untitled_test_case(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="aaa", header="bbb", footer="ccc"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

