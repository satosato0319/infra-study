※ 実行環境については README.md に記載

## やったこと
### SSH の設定、起動、鍵認証
- SSH の現在の状態を確認
```bash
sudo systemctl status ssh
```
- SSH の設定ファイルに以下を入力（既にあるなら保存して終了）
```bash
sudo nano /etc/ssh/sshd_config
```
- rootログイン禁止、パスワードログイン許可、鍵認証ログイン許可
```conf
PermitRootLogin no
PasswordAuthentication yes
PubkeyAuthentication yes
```
- 認証鍵を作成
```bash
ssh-keygen -t ed25519
```
- 公開鍵を SSH サーバーのauthorized_keys に追加（パブリックキーを明示）
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub ユーザー名@ホスト
```
- パスワードログインではなく、鍵認証でログインできるか確認
```bash
ssh ユーザー名@ホスト
```
- SSH の設定ファイルを以下に修正
```bash
sudo nano /etc/ssh/sshd_config
```
- rootログイン禁止、パスワードログイン禁止、鍵認証ログイン許可
```conf
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```
- ssh再起動
```bash
sudo systemctl reload ssh
```
## 詰まった点
- ssh-copy-id を使用して、公開鍵を authorized_keys にコピーしようとしたが、失敗
## 原因究明
- コピーを試みた際、以下のログを確認
```bash
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
```
- 上記ログから、ログインできなかったと判断し、まず設定ファイルを確認した結果、パスワード認証が無効化されていた
```bash
sudo nano /etc/ssh/sshd_config
```
- また、 authorized_keys があるかも確認した結果、存在しない
```bash
ls ~/.ssh
```
- パスワード認証が無効になっており、ssh-copy-id が利用できなかった為、手動で公開鍵を authorized_keysに追加する必要があると判断
## 対応
- 公開鍵を手動で authorized_keys にコピー
```bash
cat ~/.ssh/id_ed25519.pub >> /home/ユーザー名/.ssh/authorized_keys
```
- 上記フォルダの権限を自分のみ読み書きができるように設定
```bash
chmod 600 /home/ユーザー名/.ssh/authorized_keys
```
- 設定後、ログインできるか確認
```bash
ssh ユーザー名@localhost
```
  
## 学んだこと
- パスワード認証は、鍵認証でログインできることを確認できてから無効化する必要がある
