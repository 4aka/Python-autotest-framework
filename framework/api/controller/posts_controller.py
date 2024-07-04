from framework.api.service.api_service import Request as api

POSTS_URI = "/posts"


class PostsController:

    @staticmethod
    def get_new_posts():
        return api.send_get_request(POSTS_URI)

    @staticmethod
    def create_post(body):
        return api.send_post_request(POSTS_URI, body)

    @staticmethod
    def delete_post(post_number: int):
        return api.send_delete_request(POSTS_URI + f"/{post_number}")

    @staticmethod
    def edit_post(post_number, body):
        return api.send_put_request(POSTS_URI + f"/{post_number}", body)
