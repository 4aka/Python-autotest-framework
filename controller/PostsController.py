from framework.api.APIHelper import Request as api

POSTS_URI = "/posts"

def get_posts():
    return api.send_get_request(POSTS_URI)


def create_post(post_data):
    return api.send_post_request(POSTS_URI, post_data)


def delete_post(post_number):
    return api.send_delete_request(POSTS_URI + "/" + post_number)
