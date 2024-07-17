import pytest
from framework.api.model_builder.np_tracking_builder import TrackingBuilder as builder
from framework.api.service.np_common_servise import Request as action
from framework.api.models.np_tracking_response import TrackingResponse
from fake_functions.faker import Fake


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


@pytest.mark.api
def test_parcel_tracking(setup_module, setup_function):

    tracking_number = '20450959314437'

    # Build model
    tracking = builder.build_tracking_request(tracking_number)

    # Send request and assert 200
    response = action.send_post_request(tracking)
    assert response.status_code == 200

    # Parse response
    tracking_response = TrackingResponse.model_validate(response.json())

    # Assertions
    assert tracking_response.success
    assert len(tracking_response.errors) is 0


@pytest.mark.api
def test_parcel_number_is_incorrect(setup_module, setup_function):

    tracking_number = Fake.fake_int()

    # Build model
    tracking = builder.build_tracking_request(tracking_number)

    # Send request and assert 200
    response = action.send_post_request(tracking)
    assert response.status_code == 200

    # Parse response
    tracking_response = TrackingResponse.model_validate(response.json())

    # Assertions
    assert not tracking_response.success
    assert tracking_response.errors[0] == 'Document number is not correct'


if __name__ == '__main__':
    pytest.main()
