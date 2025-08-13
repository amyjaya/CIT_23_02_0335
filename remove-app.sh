#!/bin/bash
set -e
echo "Removing containers, images, network and volumes..."
docker compose down --rmi all -v --remove-orphans
docker network rm webnet 2>/dev/null || true
docker volume rm redis_data 2>/dev/null || true
echo "Removed."

