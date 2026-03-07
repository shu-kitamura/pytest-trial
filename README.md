# pytest のお試し

このリポジトリは、`pytest` の基本的な動かし方を確認するための小さなサンプルです。

- `conftest.py` で fixture を定義する
- `config.yml` からテスト用の設定値を読む
- テストごとに `output/` 配下へ結果を書き出す

今のテストは動作確認用の内容で、外部機器への実アクセスはしていません。

## ディレクトリ構成

```text
.
├── config.yml
├── pyproject.toml
├── src/
│   └── ft-automation/
│       └── main.py
├── tests/
│   ├── conftest.py
│   ├── lib/
│   │   └── config.py
│   ├── disk/
│   │   └── test_raid.py
│   └── network/
│       └── test_version_check.py
└── output/
```

## セットアップ

`uv` を使う前提です。

```bash
uv sync --dev
```

## テスト実行

全件実行:

```bash
uv run pytest -q
```

個別実行:

```bash
uv run pytest tests/disk/test_raid.py -q
uv run pytest tests/network/test_version_check.py -q
```

## 設定ファイル

`config.yml` にテスト用の設定を書いています。主に使っているのは次の項目です。

- `output_dir`: テスト結果の出力先
- `driver`: ドライバ名と期待バージョン
- `vmnics`: 想定する NIC 名の一覧
- `raid_parameters`: RAID テスト用のパラメータ

## 出力ファイル

各テストは `output/` 配下に `*_output.txt` を生成します。`output/` は `.gitignore` 対象です。
