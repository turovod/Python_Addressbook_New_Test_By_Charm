from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:
    db = Database()

    # class db.Entity contains field _table_
    class ORMGroup(db.Entity):
        # The _table_ - name of db table
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # For queries on several tables at the same time, when queries on one table do not need
        contacts = Set(lambda: ORMFixture.PRMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class PRMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        # For queries on several tables at the same time, when queries on one table do not need
        group = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        # Display in console generate sql request
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    #  Mark for ORM that this function should be run during the session
    @db_session # 1й вариант
    def get_group_list(self):
        # with db_session:
        #     return list(select(g for g in ORMFixture.ORMGroup))
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.PRMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

