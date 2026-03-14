from pathlib import Path
from typing import Any

import pytest
import yaml

CONFIG_PATH = Path("config.yml")


def config_load(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    with config_path.open(encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    if not isinstance(config, dict):
        raise pytest.UsageError(
            "config.yml のトップレベルは mapping である必要があります。"
        )

    return config
