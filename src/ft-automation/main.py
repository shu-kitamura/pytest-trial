from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yml"


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    if not isinstance(config, dict):
        msg = "config.yml のトップレベルは mapping である必要があります。"
        raise ValueError(msg)

    return config


def main():
    config = load_config(CONFIG_PATH)
    print(config)


if __name__ == "__main__":
    main()
