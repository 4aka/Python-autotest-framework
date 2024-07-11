import pytest
from framework.api.model_builder.np_tracking_builder import TrackingBuilder as builder
from framework.api.service.np_common_servise import Request as action
from framework.api.models.np_tracking_response import TrackingResponse


@pytest.fixture(scope='function')
def setup_function():
    print("\nSetting up function...\n")
    yield
    print("\nTearing down function...\n")


@pytest.mark.api
def test_create_post(setup_module, setup_function):

    tracking_number = ''

    # Build model
    tracking = builder.build_tracking_request(tracking_number)

    # Send request and assert 200
    response = action.send_post_request(tracking)
    assert response.status_code == 200

    # Parse response
    tracking_response = TrackingResponse.model_validate(response.json())
    parcel = tracking_response.data[0]

    # Assertions
    assert tracking_response.success
    assert parcel.Number == tracking_number


if __name__ == '__main__':
    pytest.main()
