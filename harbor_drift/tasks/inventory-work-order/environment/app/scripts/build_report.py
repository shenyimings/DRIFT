import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from inventory import load_items  # noqa: E402
from inventory.report import build_report  # noqa: E402

items = load_items(ROOT / "data.json")
out = ROOT / "out"
out.mkdir(exist_ok=True)
(out / "report.json").write_text(json.dumps(build_report(items), indent=2) + "\n")
print(f"wrote {out / 'report.json'}")
