# コードベース構造

## ディレクトリ構成
```
my-playground-neo4j/
├── scripts/              # スクリプト類
│   ├── start-neo4j.sh   # Neo4j起動スクリプト
│   └── stop-neo4j.sh    # Neo4j停止スクリプト
├── .devcontainer/       # Dev Container設定
│   ├── devcontainer.json
│   └── Dockerfile
├── .serena/            # Serenaツール設定
├── node_modules/       # Node.js依存関係（devcontainer用）
├── example.py          # メインサンプルコード
├── pyproject.toml      # Python設定・依存関係
├── uv.lock            # uvロックファイル
├── docker-compose.yml  # Docker Compose設定
├── mise.toml          # miseツール設定
├── CLAUDE.md          # プロジェクト指示書
├── README.md          # プロジェクト説明
├── LICENSE            # MITライセンス
└── .gitignore         # Git除外設定
```

## 主要ファイルの役割

### コア実装
- **example.py**: Neo4j操作のサンプル実装
  - `Neo4jExample`クラス: 主要なNeo4j操作を実装
  - 社員データベースのCRUD操作
  - 部署との関係性管理
  - 統計情報取得機能

### 設定ファイル
- **pyproject.toml**: Python設定、依存関係、ruff設定
- **docker-compose.yml**: Neo4jコンテナ設定
- **mise.toml**: uvツール管理
- **CLAUDE.md**: 開発方針・指示（日本語）

### スクリプト
- **scripts/start-neo4j.sh**: 環境自動判定のNeo4j起動
- **scripts/stop-neo4j.sh**: Neo4j停止

### 開発環境
- **.devcontainer/**: VS Code Dev Container設定
- **node_modules/**: devcontainer用のNode.js依存関係

## テスト構成
- 現在テストディレクトリは存在しない
- pytest設定は`pyproject.toml`で定義済み
- テストパス: `tests/`（作成時）