# タスク完了時のチェックリスト

## 必須チェック項目

### コード品質
```bash
# 1. リンティングチェック
uv run ruff check .

# 2. フォーマットチェック
uv run ruff format . --check

# 3. フォーマット適用（必要に応じて）
uv run ruff format .
```

### テスト実行
```bash
# 4. テスト実行（存在する場合）
uv run pytest

# 5. カバレッジ確認（推奨）
uv run pytest --cov=. --cov-report=term-missing
```

### 動作確認
```bash
# 6. Neo4j接続確認
./scripts/start-neo4j.sh

# 7. サンプルコード実行確認
uv run example.py
```

## 推奨チェック項目

### ドキュメント更新
- README.mdの更新（必要に応じて）
- CLAUDE.mdの更新（新機能追加時）
- コメント・docstringの追加・更新

### セキュリティ確認
- 機密情報の漏洩がないか確認
- Neo4jパスワードのハードコーディング回避

### パフォーマンス
- Neo4jクエリの効率性確認
- 適切なインデックス使用

## エラー対応

### よくある問題
1. **Neo4j接続エラー**: `./scripts/start-neo4j.sh`でコンテナ起動確認
2. **ポート競合**: `lsof -i :7474`でポート使用状況確認
3. **ruffエラー**: `uv run ruff format .`で自動修正を試行