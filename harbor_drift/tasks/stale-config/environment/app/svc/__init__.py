import tomllib
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "settings" / "service.toml"


def load_config():
    return tomllib.loads(CONFIG_PATH.read_text())
