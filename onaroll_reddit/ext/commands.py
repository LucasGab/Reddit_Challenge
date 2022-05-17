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


def update_posts_process():
    """Retrieve and update from top posts"""
    actual_posts = RedditPost.query.all()
    actual_posts = [post.to_dict() for post in actual_posts]

    try:
        new_posts = get_top_posts(75)

        reddit_controller.new_posts_report(new_posts, actual_posts)
        reddit_controller.deprecated_posts_report(new_posts, actual_posts)
        reddit_controller.ups_changes_posts_report(new_posts, actual_posts)

        reddit_controller.save_posts(new_posts)
    except Exception:
        print("\nTry to run again the script\n")


def init_app(app):
    for command in [create_db, drop_db, update_posts_process]:
        app.cli.add_command(app.cli.command()(command))
