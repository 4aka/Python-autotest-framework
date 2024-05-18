from framework.api.api_helper import Request as api

POSTS_URI = "/posts"


class PostsController:

    def get_new_posts():
        return api.send_get_request(POSTS_URI)

    def create_post(post_data):
        return api.send_post_request(POSTS_URI, post_data)


    def delete_post(post_number):
        return api.send_delete_request(POSTS_URI + "/" + post_number)


    def edit_post(post_number, body):
        return api.send_put_request(POSTS_URI + "/" + post_number, body)

