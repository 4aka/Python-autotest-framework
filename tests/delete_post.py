import pytest
from controller.posts_controller import PostsController as action


''' Delete post '''

def test_delete_posts():
    response = action.delete_post("1")
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
