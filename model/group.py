from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):  # string representation of an object
        # return "%s:%s" % (self.id, self.name)
        return f"{self.id}:{self.name} {self.header} {self.footer}"

    def __eq__(self, other):  # object equality rules
        # return self.id == other.id and self.name == other.name

        # if self.id is None and self.name == other.name:
        #     return True
        # elif other.id is None and self.name == other.name:
        #     return True
        # elif self.id == other.id and self.name == other.name:
        #     return True
        # else:
        #     return False

        # Transform
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return id
        else:
            return maxsize
