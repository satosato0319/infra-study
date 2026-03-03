# Linuxでのサーバー構築

## 概要

このリポジトリでは、nginx（リバースプロキシ）+ Flaskの最小限の構成で、ブラウザから nginx の'access.log'/'error.log'をボタン一つで確認できるWebアプリを作成した。ログは読み取り専用で表示する。

あわせて、UFW、SSHを有効化し、運用を意識した基本的なセキュリティ設定を行った。また、各コンポーネントの設定手順や詰まった点、切り分け手順をMarkdownファイルにまとめている。

## ドキュメント
- nginx: docs/nginx.md
- SSH: docs/ssh.md
- UFW: docs/ufw.md
- API: docs/api.md

