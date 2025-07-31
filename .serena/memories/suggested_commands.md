# 推奨コマンド

## セットアップ・環境構築
```bash
# ツールのインストール
mise install

# プロジェクト初期化
uv init

# 依存関係のインストール
uv add neo4j

# 開発依存関係のインストール
uv sync --dev
```

## Neo4j起動・停止
```bash
# Neo4j起動（推奨）
./scripts/start-neo4j.sh

# Neo4j停止
./scripts/stop-neo4j.sh

# Compose使用（代替方法）
podman-compose up -d
podman-compose down

# ログ確認
podman-compose logs -f neo4j
```

## コード実行
```bash
# メインサンプルの実行
uv run example.py

# Python直接実行
python example.py
```

## 開発・品質管理
```bash
# リンティング
uv run ruff check .

# フォーマット
uv run ruff format .

# テスト実行
uv run pytest

# カバレッジ付きテスト
uv run pytest --cov=. --cov-report=html --cov-report=term-missing
```

## システム・デバッグ
```bash
# コンテナ状態確認
podman ps
podman logs neo4j-playground

# ポート使用状況確認
lsof -i :7474
lsof -i :7687

# 環境情報
mise list
uv --version
```

## アクセス情報
- **Neo4j Browser**: http://localhost:7474
- **Bolt接続**: bolt://localhost:7687
- **認証**: neo4j / password