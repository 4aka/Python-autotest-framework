import pytest
from controller.posts_controller import PostsController as action
from builder.posts_builder import PostsModelBuilder as build

'''
Test name should start from test_
'''


''' Edit post '''
def test_edit_post():
    postForEdit = build.build_random_post_model()

    response = action.edit_post("1", postForEdit)
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main()

