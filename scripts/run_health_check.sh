
#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/system_health.log"

mkdir -p "$LOG_DIR"

{
    echo "===== Health check started: $(date '+%Y-%m-%d %H:%M:%S') ====="
    python3 "$PROJECT_DIR/system_check.py"
    echo "===== Health check finished: $(date '+%Y-%m-%d %H:%M:%S') ====="
    echo
} | tee -a "$LOG_FILE"
