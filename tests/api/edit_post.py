import pytest
from controller.posts_controller import PostsController as action
from builder.posts_builder import PostsModelBuilder as builder


def test_edit_post():
    postId: str = '102'

    # Create post
    post_data = builder.build_random_post_model()
    post_data.id = postId
    response = action.create_post(post_data.model_dump())
    assert response.status_code == 201

    # Edit post
    buildPostForEdit = builder.build_random_post_model()
    buildPostForEdit.title = "new title"
    response = action.edit_post(postId, buildPostForEdit)
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()

