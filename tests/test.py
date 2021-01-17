"""
You can auto-discover and run all tests with this command:

    $ pytest

Documentation:

* https://docs.pytest.org/en/latest/
* https://docs.pytest.org/en/latest/fixture.html
* http://flask.pocoo.org/docs/latest/testing/
"""

import pytest
from src import main


@pytest.fixture
def app():
    app = main.app
    app.debug = True
    return app.test_client()


def test_health(app):
    res = app.get("/health")
    assert res.status_code == 200
    assert b"OK" in res.data


def test_register_user_data(app):
    payload = {
        "age": "16 < x < 25"
    }

    res = app.post("/registerUserData", json=payload)

    assert res.status_code == 200
    assert b"OK" in res.data
