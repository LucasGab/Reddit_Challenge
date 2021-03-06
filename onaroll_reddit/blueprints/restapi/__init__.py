from flask import Blueprint
from flask_restful import Api

from .resources import RedditPostResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(RedditPostResource, "/post/")
    app.register_blueprint(bp)
