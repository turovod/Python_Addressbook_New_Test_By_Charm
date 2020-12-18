from random import randrange
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="mod_name"))

    old_groups = app.group.get_group_list()
    group = Group(name="modify_aaa")

    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups = app.group.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[index] = group

    def get_id(gr):
        return int(gr.id)
    # Method sorted sorts by numbers
    assert sorted(old_groups, key=get_id) == sorted(new_groups, key=get_id)


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
