import json
import os.path
import random
import string
from model.group import Group
import getopt
import sys

# Connecting custom parameters ------------------------------------------------------
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
# Connecting custom parameters ------------------------------------------------------

# default values -------------------------------------------------------------------
n = 2
f = "../data/groups.json"
# default values -------------------------------------------------------------------

# custom parameters -------------------------------------------------------------------
# Custom parameters are entered into project settings (file name / Edit configurations / Parameters)
for o, a in opts:
    if o == "-n":
       n = int(a)
    elif o == "-f":
        f = a
# custom parameters -------------------------------------------------------------------


# Random generator ------------------------------------------------------------------
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
# Random generator ------------------------------------------------------------------

# Model filled n times ------------------------------------------------------------------
# Generate n models
testdata = [Group(name="Tom", header="Tom_header", footer="Tom_footer")] + [
    Group(name=random_string("name: ", 3), header=random_string("header: ", 3), footer=random_string("footer: ", 3))
    for i in range(n)
]
# Model filled n times ------------------------------------------------------------------

# file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/groups.json')
# file = '../data/groups.json'
file = f

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

