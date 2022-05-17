import pytest

from onaroll_reddit.app import create_app, minimal_app
from onaroll_reddit.ext.commands import populate_db_test
from onaroll_reddit.ext.database import db


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.drop_all(app=app)


@pytest.fixture(scope="session")
def posts(app):
    with app.app_context():
        return populate_db_test()
