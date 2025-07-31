#!/bin/bash

# Neo4j停止スクリプト - CodespacesとローカルDocker/Podman両対応

set -e

CONTAINER_NAME="neo4j-playground"

# Docker/Podmanの判定
if command -v docker &> /dev/null && [ "${USE_DOCKER}" = "true" ]; then
    CONTAINER_CMD="docker"
    echo "Using Docker (Codespaces mode)"
elif command -v podman &> /dev/null; then
    CONTAINER_CMD="podman"
    echo "Using Podman (Local development mode)"
else
    echo "Error: Neither Docker nor Podman is available"
    exit 1
fi

# Neo4jコンテナの停止と削除
echo "Stopping Neo4j container..."
${CONTAINER_CMD} stop ${CONTAINER_NAME} 2>/dev/null || echo "Container was not running"
${CONTAINER_CMD} rm ${CONTAINER_NAME} 2>/dev/null || echo "Container was not found"

echo "Neo4j container stopped and removed successfully!"