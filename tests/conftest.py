import pytest

from pathlib import Path
from typing import Any

from tests.lib.config import config_load

CONFIG_PATH = Path("config.yml")

@pytest.fixture(scope="session")
def config(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    return config_load(config_path)

@pytest.fixture(scope="session")
def driver(config):
    return config["driver"]
