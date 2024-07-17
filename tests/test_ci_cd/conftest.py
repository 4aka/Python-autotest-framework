import pytest


@pytest.fixture(scope='module')
def setup_module():
    print("\nSetting up module...\n")
    yield
    print("\nTearing down module...\n")
