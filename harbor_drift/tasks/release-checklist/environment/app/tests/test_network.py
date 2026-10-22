import urllib.request


def test_supplier_feed_reachable():
    urllib.request.urlopen("http://supplier-feed.invalid/health", timeout=3)
