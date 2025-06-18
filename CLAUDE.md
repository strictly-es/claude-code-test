# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

このプロジェクトはFastAPIベースのWeb APIアプリケーションです。主なコンポーネント：

- `main.py`: メインのFastAPIアプリケーション
- `index.py`: AWS S3バケット一覧取得用のboto3スクリプト
- `cloud_jigyosya.csv`: クラウドファンディング関連企業のデータファイル

## 開発コマンド

### アプリケーション実行
```bash
# 開発モード（ホットリロード有効）
python main.py

# 本番モード
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker使用
```bash
# Dockerでビルド・実行
docker-compose up --build

# バックグラウンド実行
docker-compose up -d
```

### 依存関係管理
```bash
# 依存関係インストール
pip install -r requirements.txt

# boto3が必要な場合（S3機能用）
pip install boto3
```

### S3操作
```bash
# S3バケット一覧取得
python index.py
```

## アーキテクチャ

- **FastAPI**: REST APIフレームワーク
- **Docker**: コンテナ化とデプロイメント
- **boto3**: AWS S3との連携
- **uvicorn**: ASGIサーバー

## 重要な設定

- APIサーバーはポート8000で動作
- 開発時はホットリロードが有効
- Dockerコンテナ内でのPythonパス設定: `/app`