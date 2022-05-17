from onaroll_reddit.ext.database import db
from onaroll_reddit.models import RedditPost


def new_posts_report(posts: "list[dict]", saved_posts: "list[dict]") -> "list[dict]":
    """
    Function to get new posts from top posts that are not saved in database
    :param posts: The new posts retrived
    :type posts: list[dict]

    :param saved_posts: The saved posts to compare
    :type saved_posts: list[dict]

    :return: List of dict new posts with id, title and ups
    """
    new_posts = []
    print("\nNew top posts:\n")
    for post in posts:
        found = list(
            filter(lambda saved_post: saved_post["id"] == post["id"], saved_posts)
        )
        if len(found) == 0:
            new_posts.append(post)
            print(f"id: {post['id']}, title: {post['title']}, ups: {post['ups']}\n")

    if len(new_posts) <= 0:
        print("None")

    return new_posts


def deprecated_posts_report(posts: "list[dict]", saved_posts: "list[dict]"):
    """
    Function to get the posts from saved posts that are no longer on top list
    :param posts: The new posts retrived
    :type posts: list[dict]

    :param saved_posts: The saved posts to compare
    :type saved_posts: list[dict]

    :return: List of dict deprecated posts with id, title and ups
    """
    deprecated_posts = []
    print("\nDeprecated top posts:\n")
    for saved_post in saved_posts:
        found = list(filter(lambda post: saved_post["id"] == post["id"], posts))
        if len(found) == 0:
            deprecated_posts.append(saved_post)
            print(
                f"id: {saved_post['id']}, title: {saved_post['title']}, ups: {saved_post['ups']}\n"
            )

    if len(deprecated_posts) <= 0:
        print("None")

    return deprecated_posts


def ups_changes_posts_report(posts: "list[dict]", saved_posts: "list[dict]"):
    """
    Function to get posts that change their upvotes from top posts
    :param posts: The new posts retrived
    :type posts: list[dict]

    :param saved_posts: The saved posts to compare
    :type saved_posts: list[dict]

    :return: List of dict ups changed posts with id, title and ups
    """
    ups_posts = []
    print("\nUps votes changes in top posts:\n")
    for saved_post in saved_posts:
        found = list(filter(lambda post: saved_post["id"] == post["id"], posts))
        if len(found) >= 1:
            if saved_post["ups"] != found[0]["ups"]:
                ups_posts.append(found[0])
                print(
                    f"id {saved_post['id']} Changes from: {saved_post['ups']} to {found[0]['ups']} upvotes\n"
                )

    if len(ups_posts) <= 0:
        print("None")

    return ups_posts


def save_posts(posts: "list[dict]") -> None:
    """
    Function to clear posts from database and save a new list of posts
    :param posts: The new posts retrived
    :type posts: list[dict]

    :return: None
    """
    RedditPost.query.delete()
    posts_to_save = list(
        map(
            lambda val: RedditPost(id=val["id"], title=val["title"], ups=val["ups"]),
            posts,
        )
    )
    db.session.bulk_save_objects(posts_to_save)
    db.session.commit()
