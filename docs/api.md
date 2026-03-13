※ 実行環境については README.md に記載

## やったこと
### pythonを動かすための仮想環境を構築し、Flaskで動作確認
- 今回のプロジェクトフォルダを作成
```bash
mkdir -p ~/flask-btn
cd ~/flask-btn
```
- venv機能をインストールし、仮想環境を作成
```bash
sudo apt update
sudo apt install python3-venv
python3 -m venv .venv
```
- 仮想環境を有効化し、Flaskをインストール
```bash
source .venv/bin/activate
pip install flask
```
- まずWebサーバとして動作するか確認するため、AIを参考にしながら最小構成のapp.pyを用意
```Python
from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "flask success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
- 上記コードを実行し、正常に動作してるか確認。flask successが返れば成功。
```bash
python app.py
curl http://127.0.0.1:5000/
```

## HTMLを返してボタン表示
- templatesフォルダを作成
```bash
mkdir -p templates
```
- 上記フォルダ内にindex.htmlを作成し、まずはボタンを1つ表示するコードを用意
  ボタンを押すことで、 http://127.0.0.1:5000/run 宛に、Flaskへ POST リクエストを送る。
```bash
sudo nano templates/index.html
```
```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>Flask Button</title>
</head>
<body>
  <h1>ボタンテスト</h1>

  <form method="post" action="/run">
    <button type="submit">押す</button>
  </form>
</body>
</html>
```
- app.pyを、HTMLを返すように変更(追加コードのみ記載）
  render_template("index.html")により、GET リクエストを受けたら、 templates フォルダの index.html を読み込み、ブラウザへ返すようにした。
  また、 /run への POST リクエストを受けたら "OK (check server log)" を返すようにした。
```bash
nano app.py
```
```python
from flask import Flask, render_template

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/run")
def run():
    return "OK (check server log)"
```
- ブラウザで http://127.0.0.1:5000/ にアクセスし、正常に動作することを確認

## ボタンを追加し、 nginxの access.log/error.log を確認できるようにする
- index.htmlを修正し、access.log ボタンを押下時に /logs/access、error.log ボタンを押下時に /logs/error に get リクエストを送るようにした。
- コードは [`templates/index.html`](../templates/index.html) を参照

## ログへのパスを追加し、リクエストを受けたら log を読み取って返すようにする
- app.pyを修正し、リクエストを受けたら/var/log/nginx/access.log、/var/log/nginx/error.log の末尾200行を読み取り。整えて返すようにした。
- コードは [`app.py`](../app.py) を参照

## プロキシ

## gunicorn
## systemd
## 詰まった点
※ 検証の為、nginx関連ファイルを削除し、2回目の構築を実施した。
### 1.nginx関連ファイルを削除後、nginxを再インストールしたが起動失敗
### 2. インストール後、起動前にconfファイルが正常か確認するため、 'nginx-t' を実行したが以下エラーが起き、読み込み失敗
```bash
[emerg] 1937#1937: open() "/run/nginx.pid" failed (13: Permission denied)
```
## 原因究明
### 1. 2回目構築時、nginx start失敗

- インストール後、以下を実行したがconfファイルが存在しないことを確認
```bash
sudo nginx -t
```
- また、/etc/nginx/nginx.confの存在を確認したが、ファイルが存在しないことを確認
```bash
ls /etc/nginx/nginx.conf
```
- nginxは設定ファイルを読み込んで起動する為、設定ファイル不在によるエラーと断定

### 2. 'nginx -t' 実行したが失敗

- 上記エラーからpidファイルが開けないことが判明
- また、'Permission denied' から権限が足りないと判断
  
## 対応
### 1. nginx設定ファイル不在への対応

- 再インストールしたが設定ファイルが復元しなかった
- その為、 'mkdir' でフォルダを作成し、その配下にファイルを作成
- 最低限の設定を、インターネットを参考にして記述
- 以下を実行し正常に起動したことを確認
```bash
nginx -t
sudo systemctl start nginx
```
  
## 学んだこと
### 1. nginx設定ファイル

- 再インストールしても、設定ファイルが復元されないこともある。
- トラブル時は初期状態に戻すだけでなく、設定ファイルも確認する。
