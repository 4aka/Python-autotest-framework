import pytest
from framework.api.controller.posts_controller import PostsController as action
from framework.api.model_builder.posts_builder import PostsModelBuilder as builder


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


def test_edit_post(setup_module, setup_function):
    print('\nTest\n')
    assert 1 > 0

    post_id: str = '102'

    # Create post
    post_data = builder.build_random_post_model()
    post_data.id = post_id
    response = action.create_post(post_data)
    assert response.status_code == 201

    # Edit post
    build_post_for_edit = builder.build_random_post_model()
    build_post_for_edit.title = "new title"
    response = action.edit_post(post_id, build_post_for_edit)
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()

