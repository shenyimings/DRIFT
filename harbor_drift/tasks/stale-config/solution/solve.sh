#!/bin/bash
set -euo pipefail
cd /app
sed -i 's/^request_timeout = 15/request_timeout = 30/; s/^max_retries = 3/max_retries = 5/' settings/service.toml
python check_config.py
