from typing import List

import pytest
from pydantic import TypeAdapter

import controller.PostsController as resp
from builder.PostsBuilder import PostsModelBuilder as build
from models.post_response import Post


def test_get_posts():
    response = resp.get_posts()
    assert response.status_code == 200

    # Get list of posts
    list = TypeAdapter(List[Post]).validate_python(response.json())

    assert list[0].id is not None
    assert list[0].title is not None
    assert list[0].userId is not None
    assert list[0].body is not None


def test_post_posts():
    # Build model
    post_data = build.random_posts_model()

    # Overwrite value
    post_data.id = 101

    # Send request and assert 201
    response = resp.create_post(post_data.dict())
    assert response.status_code == 201

    # Assert response
    post = Post.parse_obj(response.json())

    # Assert equals each field
    assert post.userId == post_data.userId
    assert post.id == post_data.id
    assert post.title == post_data.title
    assert post.body == post_data.body


def test_delete_posts():
    response = resp.delete_post("1")
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
