import pytest
from fixture.application import Application

fixture = None


# @pytest.fixture(scope="session") Common fixture for all session
@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    elif not fixture.is_valid():
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    return fixture


# Common destroy fixture for all tests
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
