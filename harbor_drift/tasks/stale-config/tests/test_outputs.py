import subprocess
import sys
import tomllib
from pathlib import Path

APP = Path("/app")


def test_runtime_config_updated():
    cfg = tomllib.loads((APP / "settings" / "service.toml").read_text())
    assert cfg["http"]["request_timeout"] == 30
    assert cfg["http"]["max_retries"] == 5
    assert cfg["http"]["pool_size"] == 8 and cfg["logging"]["level"] == "info"


def test_check_passes():
    r = subprocess.run([sys.executable, "check_config.py"], cwd=APP, capture_output=True, text=True)
    assert r.returncode == 0 and "request_timeout=30 max_retries=5" in r.stdout, r.stdout + r.stderr
