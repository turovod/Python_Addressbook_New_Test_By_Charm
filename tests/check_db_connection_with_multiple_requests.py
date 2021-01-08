from fixture.db import DbFixture
from model.group import Group

# connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_contacts_in_group(Group(id="11"))
    for group in groups:
        print(group)
    print(len(groups))
finally:
    pass
    # db.destroy()
