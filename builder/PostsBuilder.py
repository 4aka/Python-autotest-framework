from framework.api.Functions import Fake as fake
from models.post_response import Post

class PostsModelBuilder:

    def random_posts_model(self):
        return Post(
            userId = fake.fake_id(),
            id = fake.fake_id(),
            title = fake.fake_fixed_string(10),
            body = fake.fake_fixed_string(100)
        )