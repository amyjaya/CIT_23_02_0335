#!/bin/bash
set -e
echo "Starting app..."
docker compose up -d
echo "Web app: http://localhost:5000"
echo "Admin:   http://localhost:6000"

