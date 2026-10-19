#!/bin/bash
# Run a Harbor task with plain Pi and with Pi under DRIFT, same model.
# Usage: harbor_drift/run.sh [task_dir] [n_attempts] [extra harbor args...]
set -euo pipefail
cd "$(dirname "$0")/.."
TASK=${1:-harbor_drift/tasks/inventory-work-order}
K=${2:-3}
shift $(( $# > 2 ? 2 : $# )) || true
: "${GLM_API_KEY:?set GLM_API_KEY (Z.ai coding plan, China)}"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
MODEL=zai-coding-cn/glm-5.3-flash
COMMON=(-p "$TASK" -m "$MODEL" -k "$K" -n 1 -o jobs -y
        --ae "ZAI_CODING_CN_API_KEY=$GLM_API_KEY" --ae "DRIFT_MODEL=glm-5.3-flash" "$@")

harbor run --job-name "pi-baseline-$(basename "$TASK")-$(date +%s)" -a pi "${COMMON[@]}"
harbor run --job-name "pi-drift-$(basename "$TASK")-$(date +%s)" -a harbor_drift.pi_drift.agent:DriftPi "${COMMON[@]}"
