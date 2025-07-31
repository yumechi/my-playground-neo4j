# コードスタイルと規約

## 言語・コメント
- **開発言語**: 日本語（コメント、ドキュメント、変数名など）
- **docstring**: 日本語で記述
- **ログメッセージ**: 日本語

## Pythonコーディング規約

### Ruff設定（pyproject.tomlで定義）
- **Pythonバージョン**: 3.12
- **行の長さ**: 88文字
- **引用符**: ダブルクォート (`"`)
- **インデント**: スペース4つ

### 有効なルール
- `E`: pycodestyle errors
- `W`: pycodestyle warnings  
- `F`: pyflakes
- `I`: isort（import順序）
- `B`: flake8-bugbear
- `C4`: flake8-comprehensions
- `UP`: pyupgrade

### フォーマット規約
- **インデント**: スペースのみ
- **行末改行**: 保持
- **magic trailing comma**: 使用する

### import規約
- **first-party**: `my-playground-neo4j`
- **順序**: isortルールに従う

## ファイル命名規約
- **テストファイル**: `test_*.py`
- **クラス**: `Test*`
- **テスト関数**: `test_*`

## ログ設定
- **レベル**: INFO
- **ロガー**: `__name__`を使用