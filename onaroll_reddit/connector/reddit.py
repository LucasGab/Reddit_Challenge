import requests


def get_top_posts(limit: int) -> "list[dict]":
    """
    Function to get Top daily posts from reddit
    :param limit: The total posts retrived
    :type limit: int

    :return: List of dict posts with id, title and ups
    :raises: :class:`Exception`: Unsucessfull request
    """
    response = requests.get(f"https://www.reddit.com/r/all/top/.json?limit={limit}")
    if response.status_code == 200:
        return list(
            map(
                lambda val: {
                    "id": val["data"]["id"],
                    "title": val["data"]["title"],
                    "ups": val["data"]["ups"],
                },
                response.json()["data"]["children"],
            )
        )
    else:
        print("Error trying to get information")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        raise Exception(
            {
                "Message": "Error trying to get information",
                "Response": response.json(),
                "Status_Code": response.status_code,
            }
        )
