import pytest
from framework.api.model_builder.np_tracking_builder import TrackingBuilder as builder
from framework.api.service.np_common_servise import Request as action


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


@pytest.mark.api
def test_create_post(setup_module, setup_function):

    tracking_number = '20450959314437'

    # Build model
    tracking = builder.build_tracking_request(tracking_number)

    # Send request and assert 200
    response = action.send_post_request(tracking)
    assert response.status_code == 200

    print(response.json())

    # Parse response
    # response_model = Post.model_validate(response.json())
    #
    # # Assert equals each field
    # assert response_model.userId == post_data.userId
    # assert response_model.id == post_data.id
    # assert response_model.title == post_data.title
    # assert response_model.body == post_data.body


if __name__ == '__main__':
    pytest.main()
