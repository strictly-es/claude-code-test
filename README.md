# FastAPI + AWS S3 Integration Project

FastAPIベースのWeb APIアプリケーションとAWS S3連携機能を提供するプロジェクトです。

## 機能

- **FastAPI Web API**: 基本的なHello Worldエンドポイント
- **AWS S3連携**: boto3を使用したS3バケット一覧取得機能
- **Docker対応**: コンテナ化とデプロイメント機能

## 必要要件

- Python 3.8+
- pip
- Docker & Docker Compose (オプション)
- AWS認証情報 (S3機能使用時)

## インストール

```bash
# 依存関係のインストール
pip install -r requirements.txt

# AWS S3機能を使用する場合
pip install boto3
```

## 使用方法

### 開発モード

```bash
# ホットリロード有効で起動
python main.py
```

### 本番モード

```bash
# uvicornで本番起動
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker使用

```bash
# Dockerでビルド・実行
docker-compose up --build

# バックグラウンド実行
docker-compose up -d
```

### S3バケット一覧取得

```bash
# S3バケット一覧を表示
python index.py
```

## API エンドポイント

- `GET /`: Hello Worldメッセージを返す

## プロジェクト構成

```
.
├── main.py              # FastAPIメインアプリケーション
├── index.py             # S3バケット一覧取得スクリプト
├── requirements.txt     # Python依存関係
├── Dockerfile          # Dockerイメージ設定
├── docker-compose.yml  # Docker Compose設定
├── CLAUDE.md           # Claude Code用プロジェクト設定
└── README.md           # このファイル
```

## 技術スタック

- **FastAPI**: 高性能なPython Web APIフレームワーク
- **uvicorn**: ASGI サーバー
- **boto3**: AWS SDK for Python
- **Docker**: コンテナ化プラットフォーム

## 開発

このプロジェクトは [Claude Code](https://claude.ai/code) を使用して開発されています。