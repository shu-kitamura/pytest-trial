import pytest

from collections.abc import Generator
from io import TextIOWrapper
from pathlib import Path
from typing import Any

from tests.helper.config import config_load

CONFIG_PATH = Path("config.yml")


@pytest.fixture(scope="session")
def config(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    return config_load(config_path)


@pytest.fixture(scope="session")
def output_dir(config: dict[str, Any]) -> Path:
    dir = Path(config["output_dir"])
    dir.mkdir(parents=True, exist_ok=True)
    return dir


@pytest.fixture(scope="function")
def output_file(output_dir: Path, request: pytest.FixtureRequest) -> Generator[TextIOWrapper, None, None]:
    test_name = request.node.name
    file_path = output_dir / f"{test_name}_output.txt"
    file_path.touch(exist_ok=True)
    f = file_path.open("w", encoding="utf-8")
    yield f
    f.close()
