from flask import abort, jsonify
from flask_restful import Resource

from onaroll_reddit.models import RedditPost


class RedditPostResource(Resource):
    def get(self):
        posts = RedditPost.query.all() or abort(204)
        return jsonify({"posts": [post.to_dict() for post in posts]})
