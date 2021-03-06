import random
import string
from model.group import Group


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="Tom", header="Tom_header", footer="Tom_footer")] + [
    Group(name=random_string("name: ", 3), header=random_string("header: ", 3), footer=random_string("footer: ", 3))
    for i in range(2)
]

