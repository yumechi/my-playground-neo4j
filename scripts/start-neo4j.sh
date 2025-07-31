#!/bin/bash

# Neo4j起動スクリプト - CodespacesとローカルDocker/Podman両対応

set -e

# 環境変数の設定
NEO4J_AUTH=${NEO4J_AUTH:-"neo4j/password"}
NEO4J_VERSION=${NEO4J_VERSION:-"latest"}
CONTAINER_NAME="neo4j-playground"

# Docker/Podmanの判定
if command -v docker &> /dev/null && [ "${USE_DOCKER}" = "true" ]; then
    CONTAINER_CMD="docker"
    COMPOSE_CMD="docker compose"
    echo "Using Docker (Codespaces mode)"
elif command -v podman &> /dev/null; then
    CONTAINER_CMD="podman"
    COMPOSE_CMD="podman-compose"
    echo "Using Podman (Local development mode)"
else
    echo "Error: Neither Docker nor Podman is available"
    exit 1
fi

# 既存のコンテナをクリーンアップ
echo "Cleaning up existing containers..."
${CONTAINER_CMD} stop ${CONTAINER_NAME} 2>/dev/null || true
${CONTAINER_CMD} rm ${CONTAINER_NAME} 2>/dev/null || true

# Neo4jコンテナの起動
echo "Starting Neo4j container..."
${CONTAINER_CMD} run -d \
    --name ${CONTAINER_NAME} \
    -p 7474:7474 \
    -p 7687:7687 \
    -e NEO4J_AUTH=${NEO4J_AUTH} \
    -e NEO4J_PLUGINS='["apoc"]' \
    -e NEO4J_dbms_security_procedures_unrestricted=apoc.* \
    -e NEO4J_dbms_security_procedures_allowlist=apoc.* \
    -v neo4j_data:/data \
    -v neo4j_logs:/logs \
    -v neo4j_import:/var/lib/neo4j/import \
    -v neo4j_plugins:/plugins \
    --restart unless-stopped \
    neo4j:${NEO4J_VERSION}

echo "Neo4j container started successfully!"
echo "Neo4j Browser: http://localhost:7474"
echo "Bolt connection: bolt://localhost:7687"
echo "Username: neo4j"
echo "Password: password"

# コンテナの状態確認
echo ""
echo "Container status:"
${CONTAINER_CMD} ps --filter name=${CONTAINER_NAME}