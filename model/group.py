class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):  # string representation of an object
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):  # object equality rules
        return self.id == other.id and self.name == other.name
