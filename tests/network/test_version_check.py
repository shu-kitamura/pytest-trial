import pytest

@pytest.fixture(scope="session")
def expected_vmnics(config):
    return [item["name"] for item in config["vmnics"]]

def test_version_check(driver):
    # cmd = f"{driver['name']} --version"
    result = "4.1.15.0-4vmw" # mocked result for demonstration

    assert driver["version"] == result, f"Expected driver version {driver['version']}, but got {result}"

def test_vmnic_name(expected_vmnics):
    vmnic_list = ["vmnic0", "vmnic1"] # mocked list of vmnic names for demonstration
    for vmnic in vmnic_list:
        assert vmnic in expected_vmnics, f"Expected vmnic name to be one of {expected_vmnics}, but got {vmnic}" 
