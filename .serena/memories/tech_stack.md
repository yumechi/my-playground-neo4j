# 技術スタック

## 言語・ランタイム
- **Python**: 3.12以上
- **Neo4j**: Community Edition (latest)

## パッケージ管理・ツール
- **mise**: ツールバージョン管理
- **uv**: Pythonパッケージマネージャー（高速）

## コンテナ・オーケストレーション
- **Podman**: コンテナランタイム（ローカル開発）
- **Docker**: コンテナランタイム（GitHub Codespaces）
- **Podman Compose / Docker Compose**: サービスオーケストレーション

## Pythonライブラリ
### プロダクション依存関係
- **neo4j**: Neo4jドライバー（>=5.0.0）

### 開発依存関係
- **pytest**: テストフレームワーク（>=7.0.0）
- **pytest-cov**: カバレッジレポート（>=4.0.0）
- **ruff**: リンター・フォーマッター

## データベース・拡張
- **Neo4j Community Edition**: グラフデータベース
- **APOC**: Neo4j用のプロシージャ・関数ライブラリ