import pytest
from framework.api.model_builder.posts_builder import PostsModelBuilder as build
from framework.api.controller.posts_controller import PostsController as action
from framework.api.models.create_post_model import Post


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


def test_create_post(setup_module, setup_function):
    # print('\nTest\n')
    # log.print('logging test in API test')
    # assert 1 > 0

    # Build model
    post_data = build.build_random_post_model()

    # Overwrite value
    post_data.id = 101

    # Send request and assert 201
    response = action.create_post(post_data)
    assert response.status_code == 201

    # Parse response
    response_model = Post.model_validate(response.json())

    # Assert equals each field
    assert response_model.userId == post_data.userId
    assert response_model.id == post_data.id
    assert response_model.title == post_data.title
    assert response_model.body == post_data.body


def test_create_post2(setup_module, setup_function):
    print('\nTest\n')
    assert 1 < 0


if __name__ == '__main__':
    pytest.main()
