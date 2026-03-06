import pytest
from tests.lib.config import config_load

config = config_load()
raid_parameters = config["raid_parameters"]

@pytest.mark.parametrize("raid_parameter", raid_parameters)
def test_raid_parameter(raid_parameter):
    # ここで RAID パラメータのテストを実装します。
    # 例えば、RAID レベルが正しいか、ドライブの数が適切かなどをチェックできます。
    assert "level" in raid_parameter, "RAID パラメータに 'level' が含まれている必要があります。"
    assert "drives" in raid_parameter, "RAID パラメータに 'drives' が含まれている必要があります。"
    assert isinstance(raid_parameter["drives"], list), "'drives' はリストである必要があります。"
    assert len(raid_parameter["drives"]) > 0, "RAID パラメータの 'drives' リストは空であってはなりません。"
