from pathlib import Path

from inventory.report import build_report, low_stock
from inventory.stock import load_items

DATA = Path(__file__).resolve().parent.parent / "data.json"


def test_low_stock_basic():
    items = [{"sku": "B", "qty": 1}, {"sku": "A", "qty": 0}, {"sku": "C", "qty": 9}]
    assert low_stock(items, 5) == ["A", "B"]


def test_report_shape():
    report = build_report(load_items(DATA))
    assert report["item_count"] == 5
    assert report["low_stock"] == ["BOLT-M4", "GEAR-XL"]
