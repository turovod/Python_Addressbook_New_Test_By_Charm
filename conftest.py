import pytest
from fixture.application import Application

fixture = None


# @pytest.fixture(scope="session") Common fixture for all session
@pytest.fixture
def app(request):
    global fixture
    # data for console input
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        # fixture = Application() # no console input
        fixture = Application(browser=browser, base_url=base_url)
        # fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            # fixture = Application() # no console input
            fixture = Application(browser=browser, base_url=base_url)
        # fixture.session.login(username="admin", password="secret")
    fixture.session.ensure_login(username="admin", password="secret")
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
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
