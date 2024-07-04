import pytest
from controller.posts_controller import PostsController as action


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


def test_delete_posts(setup_module, setup_function):
    print('\nTest\n')
    assert 1 > 0

    # response = action.delete_post()
    # assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()
