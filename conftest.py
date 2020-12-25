import json
import pytest
from fixture.application import Application
# warning! for the compiler to read the json file in the root directory it needs to be made working

fixture = None
target = None

# @pytest.fixture(scope="session") Common fixture for all session
@pytest.fixture
def app(request):
    global fixture
    global target
    # data for console input
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    # base_url = request.config.getoption("--baseUrl") # base_url is config_file
    if fixture is None or not fixture.is_valid():
        # fixture = Application() # no console input
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        # fixture.session.login(username="admin", password="secret")
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


# Common destroy fixture for all tests
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.session.logout()
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# data for console input
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    # parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
