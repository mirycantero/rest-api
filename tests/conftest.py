import pytest


@pytest.fixture()
def testapp():
    from main import app

    app.testing = True
    return app.test_client()
