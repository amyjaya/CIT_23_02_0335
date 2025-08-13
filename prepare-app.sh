#!/bin/bash
set -e
echo "Preparing app..."
docker network create webnet 2>/dev/null || true
docker volume create redis_data 2>/dev/null || true
docker compose build
echo "Prepared."

