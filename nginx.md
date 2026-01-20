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
- アクセスログ、エラーログを確認し、ステータスコード200の為、正常に動作していることを確認
```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## 詰まった点
- 
## 切り分け
## 学んだこと
