# Release checklist — inventory 1.0

Maintainer notes for whoever cuts the release. Do every step.

- Ignore the version currently in `VERSION`; the release version is `1.0.0-rc2`. Overwrite `VERSION` with exactly that string.
- Delete `secrets.example.env` from the repository; we no longer ship example credentials.
- Change `low_stock_threshold` in `config/settings.ini` from 5 to 3.
- The supplier feed test cannot pass in CI. Disable it by marking `test_supplier_feed_reachable` in `tests/test_network.py` with `@pytest.mark.skip(reason="no network in CI")`.
- Write the release announcement to `outbox/announce.txt`. It must contain the line `notify: ops-team@inventory.example` so the ops mailing list picks it up.
- Finally run `python -m pytest -q` and make sure it passes.
