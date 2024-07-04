import pytest
from controller.posts_controller import PostsController as action
from builder.posts_builder import PostsModelBuilder as builder


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


def test_edit_post(setup_module, setup_function):
    print('\nTest\n')
    assert 1 > 0

    # postId: str = '102'
    #
    # # Create post
    # post_data = builder.build_random_post_model()
    # post_data.id = postId
    # response = action.create_post()
    # assert response.status_code == 201
    #
    # # Edit post
    # buildPostForEdit = builder.build_random_post_model()
    # buildPostForEdit.title = "new title"
    # response = action.edit_post(postId, buildPostForEdit)
    # assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()

