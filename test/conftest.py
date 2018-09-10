import json

import pytest
from flask import Response
from flask.testing import FlaskClient
from werkzeug.utils import cached_property

from app import create_app


class JSONResponse(Response):

    @cached_property
    def json(self):
        return json.loads(self.get_data(as_text=True))


@pytest.fixture('session')
def flask_app():
    app = create_app()
    yield app


@pytest.fixture('session')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()
