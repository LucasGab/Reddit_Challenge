import time
from unittest import TextTestRunner

from onaroll_reddit.connector.reddit import get_top_posts
from onaroll_reddit.controller import reddit_controller
from onaroll_reddit.ext.database import db
from onaroll_reddit.models import RedditPost


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db_test():
    """Populate DB for testing purposes"""
    data = [
        RedditPost(id=1, title="Post 1", ups="92310"),
        RedditPost(id=2, title="Post 2", ups="13425"),
        RedditPost(id=3, title="Post 2", ups="20223"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return RedditPost.query.all()


def update_posts_process():
    """Retrieve and update from top posts"""
    actual_posts = RedditPost.query.all()
    actual_posts = [post.to_dict() for post in actual_posts]
    success = False
    total_retries = 4

    while not success and total_retries > 0:
        try:
            new_posts = get_top_posts(75)

            reddit_controller.new_posts_report(new_posts, actual_posts)
            reddit_controller.deprecated_posts_report(new_posts, actual_posts)
            reddit_controller.ups_changes_posts_report(new_posts, actual_posts)

            reddit_controller.save_posts(new_posts)
            success = TextTestRunner
        except Exception:
            total_retries = total_retries - 1
            print(
                f"\nError trying to request. Will try again. Have {total_retries} retries remaining\n"
            )
            time.sleep(4)


def init_app(app):
    for command in [create_db, drop_db, update_posts_process]:
        app.cli.add_command(app.cli.command()(command))
