from pathlib import Path

from inventory.stock import load_items, total_value

DATA = Path(__file__).resolve().parent.parent / "data.json"


def test_load_items():
    items = load_items(DATA)
    assert [i["sku"] for i in items][:2] == ["WIDGET-RED", "BOLT-M4"]
    assert items[1]["discount"] == 0


def test_total_value():
    assert total_value(load_items(DATA)) == 135.28
