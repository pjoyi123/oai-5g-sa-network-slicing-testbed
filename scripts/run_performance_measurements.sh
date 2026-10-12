#!/usr/bin/env bash
# Illustrative commands only: replace placeholders and verify endpoint, direction and permissions.
set -euo pipefail
: "${TARGET_IP:?Set TARGET_IP to the tested endpoint}"
: "${IPERF_SERVER:?Set IPERF_SERVER to the iPerf3 server address}"
PROFILE="${PROFILE:-eMBB}"
RUN="${RUN:-1}"
mkdir -p raw
ping -c 100 "$TARGET_IP" | tee "raw/${PROFILE}_run${RUN}_ping.txt"
iperf3 -c "$IPERF_SERVER" -t 20 -J > "raw/${PROFILE}_run${RUN}_tcp.json"
iperf3 -c "$IPERF_SERVER" -u -b 10M -t 20 -J > "raw/${PROFILE}_run${RUN}_udp.json"
# Collect Docker stats separately with verified container names and sampling intervals.
