from framework.api.api_helper import Request as apiHelper

POSTS_URI = "/posts"


def get_posts():
    return apiHelper.send_get_request(POSTS_URI)


def create_post(post_data):
    return apiHelper.send_post_request(POSTS_URI, post_data)


def delete_post(post_number):
    return apiHelper.send_delete_request(POSTS_URI + "/" + post_number)
