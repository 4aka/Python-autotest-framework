from framework.api.controller.posts_controller import PostsController as action
from typing import List
from pydantic import TypeAdapter
from framework.api.models.create_post_model import Post
import pytest


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


@pytest.mark.api
def test_get_posts(setup_module, setup_function):
    print('\nTest\n')
    assert 1 > 0

    # Get new posts
    response = action.get_new_posts()
    assert response.status_code == 200

    # Get list of posts
    posts_list = TypeAdapter(List[Post]).validate_python(response.json())

    # Assertions
    assert posts_list[0].id is not None
    assert posts_list[0].title is not None
    assert posts_list[0].userId is not None
    assert posts_list[0].body is not None


if __name__ == '__main__':
    pytest.main()

