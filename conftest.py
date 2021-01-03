import importlib
import json
import pytest
from fixture.application import Application
import os.path # for path to the config_file
from fixture.db import DbFixture
from model.group import Group
import Json
# warning! for the compiler to read the json file in the root directory it needs to be made working
# or __file__

fixture = None
target = None
group_from_json = None

# @pytest.fixture(scope="session") Common fixture for all session
@pytest.fixture
def app(request):
    global fixture
    global target
    global group_from_json
    # data for console input
    browser = request.config.getoption("--browser")
    if target is None:
        # Glue the absolute path to the project and the relative path to the file
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    # base_url = request.config.getoption("--baseUrl") # base_url is config_file
    if fixture is None or not fixture.is_valid():
        # fixture = Application() # no console input
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        # fixture.session.login(username="admin", password="secret")
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


# fixture for database connection
@pytest.fixture(scope="session")
def db(request):
    # db_config = load_config(request.config.getoption("--target"))
    db_config = {"host": "127.0.0.1",  "name": "addressbook", "user": "root"}
    db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password="")

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


# Common destroy fixture for all tests
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.session.logout()
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# data for console input and json config file
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    # parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata