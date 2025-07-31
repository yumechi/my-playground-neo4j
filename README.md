# Neo4j Playground

Neo4jデータベースを使用した実験・学習用のプロジェクトです。

**⚠️ 重要: このプロジェクトは学習・実験目的のみで作成されています。商用利用は想定していません。**

## 必要な環境

- [mise](https://mise.jdx.dev/) - ツールバージョン管理
- [Podman](https://podman.io/) - コンテナランタイム
- [Podman Compose](https://github.com/containers/podman-compose) - Docker Compose互換ツール

## セットアップ

### 1. 開発環境の準備

```bash
# miseでuvをインストール
mise install

# プロジェクトの初期化
uv init

# 依存関係のインストール
uv add neo4j
```

### 2. Neo4jの起動

```bash
# Podman Composeを使用してNeo4jを起動
podman-compose up -d

# ログの確認
podman-compose logs -f neo4j
```

### 3. Neo4jの停止

```bash
# サービスの停止
podman-compose down

# データも含めて完全に削除する場合
podman-compose down -v
```

## アクセス方法

- **Neo4j Browser**: http://localhost:7474
- **Bolt接続**: bolt://localhost:7687
- **認証情報**: 
  - ユーザー名: `neo4j`
  - パスワード: `password`

## Python での使用例

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

## トラブルシューティング

### Podman Composeが見つからない場合

```bash
# Podman Composeのインストール（Ubuntu/Debian）
sudo apt install podman-compose

# または pip経由でインストール
pip install podman-compose
```

### ポートが使用されている場合

```bash
# 使用中のポートを確認
podman ps
lsof -i :7474
lsof -i :7687

# 既存のコンテナを停止
podman stop neo4j-playground
podman rm neo4j-playground
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

### 使用しているソフトウェアのライセンスについて

- **Neo4j Community Edition**: GPL v3ライセンス
- **このプロジェクトのコード**: MITライセンス

このプロジェクトは学習・実験目的で作成されており、Neo4j Community Editionをクライアントライブラリ経由で使用しています。Neo4jのライセンス要件については[Neo4j公式サイト](https://neo4j.com/licensing/)を参照してください。