※ 実行環境については README.md に記載

## やったこと
### ufwのインストール、有効化、状態確認
- aptパッケージを最新版にアップデート
```bash
sudo apt update
```
- WSL（Ubuntu）上に ufw をインストール
```bash
sudo apt install ufw -y
```
- ufw で SSH を許可する為、SSH サーバーも事前にインストール
```bash
sudo apt install openssh-server -y
```
- ufwで SSH と nginx を許可し、有効化後にルールが反映されているか確認
```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

## ※詰まった点、原因究明、対応、学んだこと
### [`troubleshooting.md`](./troubleshooting.md) に記載
