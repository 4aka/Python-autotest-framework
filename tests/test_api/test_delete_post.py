import pytest
from framework.api.controller.posts_controller import PostsController as action
from framework.api.model_builder.posts_builder import PostsModelBuilder as build


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


def test_delete_posts(setup_module, setup_function):
    print('\nTest\n')
    assert 1 > 0

    # Create post
    post_data = build.build_random_post_model()
    post_data.id = 101
    response = action.create_post(post_data)
    assert response.status_code == 201

    # Delete post
    response = action.delete_post(post_data.id)
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
