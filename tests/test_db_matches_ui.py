from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip()) # delete spaces
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=lambda gr: gr.id) == sorted(db_list, key=lambda gr: gr.id)
