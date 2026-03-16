# Linuxでのサーバー構築

## 概要

WSL(Ubuntu)上で、 nginx / SSH / UFW を構築し、再現手順とその構築で詰まった点や原因切り分けをMarkdownにまとめたリポジトリ。
また、ブラウザでアクセスし、ボタンを押すことで nginx のログを確認できるアプリを作成し、リバースプロキシや gunicorn、 systemd の動作原理、通信の流れを理解する。

## 環境
- Windows : Windows 11 Home
- WSL : Ubuntu 24.04
- nginx : 1.24.0
- Python : 3.12.3

## 目的
- nginxを80番ポートで動かし、ログ（access/error)を確認できる状態にする
- SSHを鍵認証でログインできるようにし、UFWでポート制限をし、最低限のセキュリティ設定を行う
- Flaskで nginx の access.log / error.log をブラウザからボタン一つで確認できるサイトを作成する。
- nginx をリバースプロキシとして動かし、上記サイトにアクセスできるようにする。
- gunicornをインストールし、nginx からリクエストを受けとるようにする。
- systemdを有効化し、運用を前提とした構成にする。

## 構成
ここに構成図を置く

## ドキュメント
- nginx: docs/nginx.md
- ssh: docs/ssh.md
- ufw: docs/ufw.md
- api: docs/api.md
- python: app.py
- html: templates/index.html

