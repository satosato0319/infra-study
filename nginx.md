※ 実行環境については README.md に記載

## やったこと
### nginxのインストールと起動、状態確認
- aptパッケージを最新版にアップデート
```bash
sudo apt update
```
- WSL（Ubuntu）上に nginx をインストールし、webサーバとして起動
```bash
sudo apt install nginx -y
sudo nginx -t
sudo systemctl start nginx
```
- wsl再起動時、自動起動に設定
```bash
sudo systemctl enable nginx
```
- nginxの状態確認(active (running)を確認)
```bash
sudo systemctl status nginx
```

### HTML表示確認
- htmlフォルダ確認(index.nginx-debian.htmlのみを確認)
```bash
ls /var/www/html
```
- htmlファイル作成
```bash
sudo nano /var/www/html/index.html
```
- 以下をファイル内に記述(ctrl+oで保存、ctrl+xで終了)
```html
<h1>Hello, this is test.</h1>
```
- ブラウザでhttp://localhostにアクセス
- アクセスログ、エラーログを確認し、ステータスコード200の場合、正常に動作していることとする
```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## 詰まった点
※ 検証の為、nginx関連ファイルを削除し、2回目の構築を実施した。
- 1. nginx関連ファイルを削除後、nginxを再インストールしたが起動失敗
## 原因究明
- 1. 2回目構築時、nginx start失敗

- インストール後、以下を実行したがconfファイルが存在しないことを確認
```bash
nginx -t
```
- また、/etc/nginx/nginx.confの存在を確認したが、ファイルが存在しないことを確認
```bash
ls /etc/nginx/nginx.conf
```
- nginxは設定ファイルを読み込んで起動する為、設定ファイル不在によるエラーと断定

## 対応
### 1. nginx設定ファイル不在への対応

- 再インストールしたが設定ファイルが復元しなかった
- その為、 'mkdir'でフォルダを作成し、その配下にファイルを作成
- 最低限の設定を、インターネットを参考にして記述
- 以下を実行し正常に起動したことを確認
```bash
nginx -t
sudo systemctl start nginx
```
  
## 学んだこと
