# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="aaa", header="bbb", footer="ccc")
    app.group.create(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert old_groups == new_groups

    # Compare sorted groups (optional)
    def id_or_max(gr):
        if gr.id is None:
            gr.id = new_groups[len(new_groups) - 1].id
        return gr.id

    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="1", header=" ", footer=" ")
    app.group.create(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert new_groups == old_groups
