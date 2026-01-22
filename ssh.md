※ 実行環境については README.md に記載

## やったこと
### SSH の設定、起動、
- SSH の設定ファイルに、以下を入力
- rootログイン禁止、パスワードログイン許可
```bash
sudo nano /etc/ssh/sshd_config
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

## 詰まった点
- 今回の設定では、特に詰まった点はなかった
## 注意した点
- ufw ではポート番号で許可指定する方法と、プロファイルで許可指定する方法があるが、表記を揃えるためプロファイルで許可した
- 許可後に ufw を有効化することで、nginx と SSH の通信切断が起こらないようにした
  
## 学んだこと
- 有効化後は、許可状態を確認することで、ルールが正しいか判断できる。
