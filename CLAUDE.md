# Neo4j Playground プロジェクト

このリポジトリは Neo4j データベースを使用した実験・学習用のプロジェクトです。

このプロジェクトでのコミュニケーションは日本語で行います。

## 環境構成

- **コンテナランタイム**: Podman
- **データベース**: Neo4j
- **プログラミング言語**: Python(バージョン 3.12)
- **パッケージマネージャー**: uv (mise経由でインストール)
- **Neo4j Python ライブラリ**: neo4j-driver

## セットアップ

### 開発環境の準備

```bash
# miseでuvをインストール
mise install

# プロジェクトの初期化
uv init

# 依存関係のインストール
uv add neo4j
```

### Neo4j の起動

#### 簡単な起動方法（推奨）

```bash
# Neo4j起動
./scripts/start-neo4j.sh

# Neo4j停止
./scripts/stop-neo4j.sh
```

#### 環境別の起動方法

**GitHub Codespaces:**
- Docker-in-Dockerを使用
- 自動的にDockerが選択される

**ローカル開発:**
- Podmanを使用
- 手動でコンテナを起動する場合：

```bash
podman run -d \
  --name neo4j-playground \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  -e NEO4J_PLUGINS='["apoc"]' \
  -e NEO4J_dbms_security_procedures_unrestricted=apoc.* \
  -e NEO4J_dbms_security_procedures_allowlist=apoc.* \
  -v neo4j_data:/data \
  -v neo4j_logs:/logs \
  -v neo4j_import:/var/lib/neo4j/import \
  -v neo4j_plugins:/plugins \
  neo4j:latest
```

## 基本的な使用方法

Neo4j への接続とクエリ実行のサンプル:

```python
from neo4j import GraphDatabase

# データベース接続
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# セッション使用例
def example_query(tx):
    result = tx.run("MATCH (n) RETURN count(n) as count")
    return result.single()["count"]

with driver.session() as session:
    count = session.execute_read(example_query)
    print(f"ノード数: {count}")

driver.close()
```

## アクセス情報

- **Neo4j Browser**: http://localhost:7474
- **Bolt接続**: bolt://localhost:7687
- **認証**: neo4j / password