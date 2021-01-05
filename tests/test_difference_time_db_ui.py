from model.group import Group
from timeit import timeit


def test_time_db_ui(app, db):
    print()
    print(timeit(lambda: app.group.get_group_list(), number=1))
    print(timeit(lambda: db.get_group_list(), number=1000))

    assert False # Displaying results in the console
