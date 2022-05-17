def test_posts_get_all(client, posts):
    """Test get all posts"""
    response = client.get("/api/v1/post/")
    assert response.status_code == 200
    data = response.json
    assert len(data["posts"]) == len(posts)
