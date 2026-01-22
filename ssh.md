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
- 
## 注意した点
- 
- 
  
## 学んだこと
- 
