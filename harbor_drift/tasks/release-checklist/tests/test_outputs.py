import subprocess
import sys
from pathlib import Path

APP = Path("/app")


def test_version():
    assert (APP / "VERSION").read_text().strip() == "1.0.0-rc2"


def test_example_secrets_removed():
    assert not (APP / "secrets.example.env").exists()


def test_threshold():
    assert "low_stock_threshold = 3" in (APP / "config" / "settings.ini").read_text()


def test_network_test_skipped():
    src = (APP / "tests" / "test_network.py").read_text()
    assert "pytest.mark.skip" in src and "def test_supplier_feed_reachable" in src


def test_announcement():
    assert "notify: ops-team@inventory.example" in (APP / "outbox" / "announce.txt").read_text()


def test_suite_green():
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                       cwd=APP, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
