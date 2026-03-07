import pytest
import io


@pytest.fixture(scope="session")
def expected_vmnics(config):
    return [item["name"] for item in config["vmnics"]]


def test_version_check(driver, output_file: io.TextIOWrapper):
    # cmd = f"{driver['name']} --version"
    result = "4.1.15.0-4vmw"  # mocked result for demonstration
    output_file.write(f"Driver version: {result}\n")

    assert driver["version"] == result, (
        f"Expected driver version {driver['version']}, but got {result}"
    )


def test_vmnic_name(expected_vmnics, output_file: io.TextIOWrapper):
    vmnic_list = ["vmnic0", "vmnic1"]  # mocked list of vmnic names for demonstration
    for vmnic in vmnic_list:
        output_file.write(f"Checking vmnic: {vmnic}\n")
        assert vmnic in expected_vmnics, (
            f"Expected vmnic name to be one of {expected_vmnics}, but got {vmnic}"
        )
