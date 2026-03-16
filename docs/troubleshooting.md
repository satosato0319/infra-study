# 各マークダウンファイルの詰まった点や原因究明、学んだこと等を記載

# nginx
## 詰まった点
※ 検証の為、nginx 関連ファイルを削除し、2回目の構築を実施した。

### 1つ目 nginx 関連ファイルを削除後、nginx を再インストールしたが起動に失敗した。

### 2つ目 インストール後、起動前に設定ファイルが正常か確認するため、 'nginx -t' を実行したが以下エラーが起き、読み込みに失敗した。
```bash
[emerg] 1937#1937: open() "/run/nginx.pid" failed (13: Permission denied)
```
## 確認したこと
### 1. 2回目構築時、nginx 起動失敗

- 以下を実行したが設定ファイルが存在しなかった
```bash
sudo nginx -t
```
- また、/etc/nginx/nginx.confの存在を確認したが、ファイルが存在しなかった
```bash
ls /etc/nginx/nginx.conf
```
- nginxは設定ファイルを読み込んで起動する為、設定ファイル不在が起動失敗の要因と判断した

### 2. 'nginx -t' 実行したが失敗

- 上記エラーからpidファイルが開けないことが判明
- また、'Permission denied' から権限が足りないと判断
  
## 対応
### 1. nginx設定ファイル不在への対応

- 再インストールしたが設定ファイルが復元されなかった
- その為、 フォルダとその配下にファイルを作成し、最低限の設定を記述した
- その後、以下を実行し正常に起動することを確認した
```bash
nginx -t
sudo systemctl start nginx
```
### 2. 権限エラーへの対応
- sudo をつけるの忘れていた為、再度 sudo をつけて実行したら、確認できた。
- 
## 学んだこと
### 1. nginx設定ファイル

- 再インストールしても、設定ファイルが復元されない場合がある。
- トラブル時は、初期状態に戻すだけでなく、設定ファイルも確認することが重要。

### 2. 権限エラー
- `Permission denied` と表示された場合は、まず権限不足を疑う。
- コマンドによっては一般ユーザーで実行できない場合があるため、`sudo` が必要実行前に確認する。

# ssh
## 詰まった点
### ssh-copy-id を使用して、公開鍵を authorized_keys にコピーしようとしたが、失敗
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

# ufw
## 詰まった点
- 今回の設定では、特に詰まった点はなかった
## 注意した点
- ufw ではポート番号で許可指定する方法と、プロファイルで許可指定する方法があるが、表記を揃えるためプロファイルで許可した
- 許可後に ufw を有効化することで、nginx と SSH の通信切断が起こらないようにした
  
## 学んだこと
- 有効化後は、許可状態を確認することで、ルールが正しいか判断できる。

# api
## 詰まった点
### 1. `python3 -m venv .venv` を実行しようしたが、`ensurepip is not available` とエラーコードが表示され、仮想環境作成に失敗した。
### 2. `render_template("index.html")` 実行時に `index.html` が見つからず、画面表示に失敗した。
## 確認したこと
### 1. 仮想環境作成失敗
- エラーコードから `python3-venv` をインストールする必要があることを確認した
### 2. index.html 不在
- `templates` ディレクトリ内を確認したところ、ファイル名が`index.html` ではなく `intex.html` だった。
## 対応
### 1. 仮想環境作成失敗
- 以下コマンドで  `python3-venv` をインストールした
```bash
sudo apt update
sudo apt install python3-venv
```
### 2. index.html 不在
-  `templates/intex.html` を `templates/index.html` に名前を修正した
## 学んだこと
### 1. 仮想環境作成失敗
- ubuntu では 最低限の機能しか用意されていないため、仮想環境作成用のパッケージをインストールする必要がある。

### 2. index.html 不在
- Flaskは `render_template("index.html")` で指定したファイル名を探すため、ファイル名のスペルミスに注意する。
