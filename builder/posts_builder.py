from framework.helpers import Fake as fake
from models.post_response import Post

class PostsModelBuilder:

    def build_random_post_model():
        return Post(
            userId = fake.fake_id(),
            id = fake.fake_id(),
            title = fake.fake_fixed_string(10),
            body = fake.fake_fixed_string(100)
        )