from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None,
                 fax=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return f"{self.id}: {self.firstname} {self.lastname}"

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return id
        else:
            return maxsize
