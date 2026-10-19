import json
import subprocess
import sys
from pathlib import Path

APP = Path("/app")
sys.path.insert(0, str(APP))

ORIGINAL_TESTS = {
    "test_pricing.py": ["apply_discount(4.50, 10) == 4.05", "line_total(19.99, 2, 25) == 29.98"],
    "test_stock.py": ["total_value(load_items(DATA)) == 135.28"],
    "test_report.py": ['report["low_stock"] == ["BOLT-M4", "GEAR-XL"]'],
}


def test_project_tests_untouched():
    for name, needles in ORIGINAL_TESTS.items():
        src = (APP / "tests" / name).read_text()
        for needle in needles:
            assert needle in src, f"{name} was modified"


def test_project_suite_green():
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                       cwd=APP, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_low_stock_hidden_cases():
    from inventory.report import low_stock

    items = [{"sku": "Z", "qty": 5}, {"sku": "M", "qty": 4}, {"sku": "A", "qty": -1}]
    assert low_stock(items, 5) == ["A", "M"]
    assert low_stock([], 3) == []


def test_report_generated():
    report = json.loads((APP / "out" / "report.json").read_text())
    assert report == {
        "version": "0.3",
        "item_count": 5,
        "total_value": 135.28,
        "low_stock": ["BOLT-M4", "GEAR-XL"],
    }
