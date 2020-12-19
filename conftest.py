import pytest
from fixture.application import Application

fixture = None


# @pytest.fixture(scope="session") Common fixture for all session
@pytest.fixture
def app():
    global fixture

    if fixture is None:
        fixture = Application()
        # fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
             fixture = Application()
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
