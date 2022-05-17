from sqlalchemy_serializer import SerializerMixin

from onaroll_reddit.ext.database import db


class RedditPost(db.Model, SerializerMixin):
    id = db.Column(db.String(140), primary_key=True)
    title = db.Column(db.String(512))
    ups = db.Column(db.Integer)
