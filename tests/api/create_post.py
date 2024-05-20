import pytest
from builder.posts_builder import PostsModelBuilder as build
from controller.posts_controller import PostsController as action
from models.create_post_model import Post


def test_create_post():
    # Build model
    post_data = build.build_random_post_model()

    # Overwrite value
    post_data.id = 101

    # Send request and assert 201
    response = action.create_post(post_data.model_dump())
    assert response.status_code == 201

    # Parse response
    responseModel = Post.model_validate(response.json())

    # Assert equals each field
    assert responseModel.userId == post_data.userId
    assert responseModel.id == post_data.id
    assert responseModel.title == post_data.title
    assert responseModel.body == post_data.body


if __name__ == '__main__':
    pytest.main()
