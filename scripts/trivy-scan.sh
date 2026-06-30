#!/bin/bash
set -e

IMAGE="data-gate-api:latest"

echo "Scanning $IMAGE..."
trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 $IMAGE
