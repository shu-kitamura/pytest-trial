import pytest
import io


@pytest.mark.log
def test_version_check(config, output_file: io.TextIOWrapper):
    # cmd = f"{driver['name']} --version"
    result = "1.0.0"  # mocked result for demonstration
    output_file.write(f"Driver version: {result}\n")

    assert config.driver.version == result, (
        f"Expected driver version {config.driver.version}, but got {result}"
    )

    assert config.base_url == f"http://192.168.1.10"


@pytest.mark.log
def test_vmnic_name(config, output_file: io.TextIOWrapper):
    expected_vmnics = config.nic.vmnics
    vmnic_list = ["vmnic0", "vmnic1"]  # mocked list of vmnic names for demonstration
    for vmnic in vmnic_list:
        output_file.write(f"Checking vmnic: {vmnic}\n")
        assert vmnic in expected_vmnics, (
            f"Expected vmnic name to be one of {expected_vmnics}, but got {vmnic}"
        )
