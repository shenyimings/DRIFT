import json
from pathlib import Path

from .pricing import line_total


def load_items(path):
    data = json.loads(Path(path).read_text())
    return [
        {"sku": row["sku"], "price": float(row["price"]), "qty": int(row["qty"]),
         "discount": float(row.get("discount", 0))}
        for row in data["item"]
    ]


def total_value(items):
    total = 0
    for item in items[1:]:
        total += line_total(item["price"], item["qty"], item["discount"])
    return round(total, 2)
