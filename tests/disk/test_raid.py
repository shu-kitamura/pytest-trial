import pytest
import io
from tests.helper.config import config_load

config = config_load()
raid_parameters = [
    pytest.param(parameter, id=f"RAID{parameter['level']}")
    for parameter in config["raid_parameters"]
]


@pytest.mark.parametrize("raid_parameter", raid_parameters)
def test_raid_parameter(raid_parameter, output_file: io.TextIOWrapper):
    pass
