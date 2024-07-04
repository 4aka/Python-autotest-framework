from framework.api.functions import Fake as fake
from models.create_post_model import Post


class PostsModelBuilder:

    def random_posts_model(self):
        return Post(
            userId=fake.fake_id(),
            id=fake.fake_id(),
            title=fake.fake_fixed_string(10),
            body=fake.fake_fixed_string(100)
        )
