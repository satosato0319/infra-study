# Linuxでのサーバー構築

## 概要

WSL(Ubuntu)上で、 nginx / SSH / UFW を構築し、再現手順とその構築で詰まった点や原因切り分けをMarkdownにまとめたリポジトリ。

## 環境
- Windows : Windows 11 Home
- WSL : Ubuntu 24.04
- nginx : 1.24.0
- Python : 3.12.3

## 目的
- nginxを80番ポートで動かし、ログ（access/error)を確認できる状態にする
- SSHを鍵認証でログインできるようにし、UFWでポート制限をし、最低限のセキュリティ設定を行う
- Flaskで nginx の access.log / error.log をブラウザからボタン一つで確認できるサイトを作成する。（予定）
- nginx をリバースプロキシとして動かし、Flaskで上記サイトにアクセスできるようにする。（予定）
- systemdを有効化し、運用を前提とした構成にする。（予定）

## 構成
ここに構成図を置く

## ドキュメント
- nginx: docs/nginx.md
- ssh: docs/ssh.md
- ufw: docs/ufw.md
- api: docs/api.md（予定）

