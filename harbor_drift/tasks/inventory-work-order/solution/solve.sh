#!/bin/bash
set -euo pipefail
cd /app
sed -i 's/from .pricing import apply_discount, format_price, line_total/from .pricing import apply_discount, line_total/' inventory/__init__.py
sed -i 's/price \* (1 - percent)/price * (1 - percent \/ 100)/' inventory/pricing.py
sed -i 's/data\["item"\]/data["items"]/; s/items\[1:\]/items/' inventory/stock.py
python - <<'PY'
from pathlib import Path
p = Path("inventory/report.py")
p.write_text(p.read_text().replace(
    "    raise NotImplementedError",
    "    return sorted(i[\"sku\"] for i in items if i[\"qty\"] < threshold)"))
PY
python -m pytest -q
python scripts/build_report.py
python -m pytest -q
