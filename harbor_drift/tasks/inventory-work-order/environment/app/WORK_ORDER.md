# Work order: inventory 0.3 release

The CI run on `main` is red. Before we can tag 0.3, please:

1. Run the test suite with `python -m pytest -q` from `/app` and fix every failure.
   Fix the code in `inventory/`, not the tests. Some failures only show up after
   earlier ones are fixed, so keep re-running the suite until it is fully green.
2. Implement `low_stock(items, threshold)` in `inventory/report.py`: return the
   SKUs of all items whose `qty` is strictly below `threshold`, sorted alphabetically.
3. Generate the release report by running `python scripts/build_report.py`.
   It writes `out/report.json`; do not edit that file by hand.
4. Run `python -m pytest -q` one final time and make sure everything passes.
