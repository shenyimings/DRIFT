from .stock import total_value


def low_stock(items, threshold):
    return sorted(i["sku"] for i in items if i["qty"] < threshold)


def build_report(items, threshold=5):
    return {
        "version": "0.3",
        "item_count": len(items),
        "total_value": total_value(items),
        "low_stock": low_stock(items, threshold),
    }
