from fake_functions.faker import Fake as faker
from framework.api.models.create_post_model import Post


class PostsModelBuilder:

    @staticmethod
    def build_random_post_model():
        return Post(
            userId=faker.fake_id(),
            id=faker.fake_id(),
            title=faker.fake_fixed_string(10),
            body=faker.fake_fixed_string(100)
        )

    # def build_model_for_edit_post(buildModel): # TODO how to use built model with fields
    #     Post: model = buildModel
    #
    #     return Edit(
    #         userId=model.userId,
    #         id=model.id,
    #         title=model.title,
    #         body=model.body
    #     )
