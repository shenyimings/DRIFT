from svc import CONFIG_PATH, load_config

cfg = load_config()["http"]
assert isinstance(cfg["request_timeout"], int) and 1 <= cfg["request_timeout"] <= 120, "bad request_timeout"
assert isinstance(cfg["max_retries"], int) and 0 <= cfg["max_retries"] <= 10, "bad max_retries"
print(f"OK {CONFIG_PATH.name}: request_timeout={cfg['request_timeout']} max_retries={cfg['max_retries']}")
