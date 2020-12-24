# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="Tom", header="Tom_header", footer="Tom_footer")] + [
    Group(name=random_string("name: ", 3), header=random_string("header: ", 3), footer=random_string("footer: ", 3))
    for i in range(2)
]


# IDs - Different options for test IDs
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_new_group(app, group):
    pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # assert len(old_groups) + 1 == len(new_groups)
    assert len(old_groups) + 1 == app.group.count()  # faster
    new_groups = app.group.get_group_list()
    _id = 0
    for i in new_groups:
        if int(i.id) > _id:
            _id = int(i.id)
    group.id = str(_id)
    old_groups.insert(0, group)
    assert sorted(old_groups, key=lambda group: group.id) == sorted(new_groups, key=lambda group: group.id), f"old_groups {old_groups} == new_groups {new_groups}"

# 5 - 4 14:30
