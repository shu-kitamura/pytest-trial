from pathlib import Path

import yaml
from pydantic import BaseModel, computed_field, ConfigDict


class HostConfig(BaseModel):
    address: str
    user: str
    password: str


class GuestConfig(BaseModel):
    address: str


class DriverConfig(BaseModel):
    name: str
    version: str


class NicConfig(BaseModel):
    vmnics: list[str]


class DacConfig(BaseModel):
    drives: list[str]

class Config(BaseModel):
    machine: str
    card: str
    host: HostConfig
    guest: GuestConfig
    output_dir: str
    driver: DriverConfig
    nic: NicConfig | None = None
    dac: DacConfig | None = None

    model_config = ConfigDict(extra="forbid")

    @computed_field
    @property
    def base_url(self) -> str:
        return f"http://{self.host.address}"

CONFIG_PATH = Path("config.yml")


def config_load(config_path: Path = CONFIG_PATH) -> Config:
    with config_path.open(encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    return Config(**data)
