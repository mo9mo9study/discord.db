# 当リポジトリの自作パッケージを使うための準備
```py
pip install mo9mo9db
# https://pypi.org/project/mo9mo9db/

# このパッケージを使用する側のディレクトリに.envのファイルを作成する
# .envファイル内に以下のDB情報とパラメータ情報を入力することが必須
vi .env
> .env ------------------------
###==============================
#MYSQL credential
###==============================
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
DB_DATABASE=''
DB_ECHO=''
------------------------------
```

# about
```
ddl/
    master/create_table.sql : DDL文。これをDBに流し込めば本番環境と同じ状態になるよう保つ。
    patch/ : TBD。migrationの仕組みが導入されるまで、DBスキーマ変更用DDLはここに置く。レビュー完了後masterのDDLにも反映する。
ERD/
    draw.ioで書かれたERD
```

# commit時のローカル運用
- ディレクトリ[.githooks/]にてcommitをトリガーに動く処理を記載しています
  - pythonの[autopep8]と[flake8]をcommit対象のファイルに対して実行します
- これを活用することでpepに準拠するように自動修正やエラー箇所を出力してくれます
- ファイル[.githooks/pre-commit]はファイル[.pre-commit-config.yaml]を元に作成されています
```py
# pre-commitを活用するための準備
## git configのコマンドを用いて、.git/hooksのパスを変更します
git config core.hooksPath .githooks
```

# Future
-

# Githubのタグ付ルールとpypiのバージョン一致について
- バージョン記法：x.y.z

| バージョン | 名称 | 説明 |
| :------- | :--- | :-- |
| x | メジャーバージョン | ほとんど使わないと思われる、破壊的な機能変更の場合に更新 |
| y | マイナーバージョン | pypiにアップロードする。テーブルの追加など本番環境で適用される機能が新たに追加がされた場合に更新 |
| z | リビジョン?       | test.pypiにアップロードする時。試験的な変更があった時 |

- Githubのタグ付方法
```sh
# v0.0.20のタグを付与する場合
# 通常のpushではtagは付与されないので別途pushが必要
# タグ付作業は(test.)pypiにアップロード後を想定
## git tag': git tag -a v0.0.31 -m "https://test.pypi.org/project/mo9mo9db/0.0.31/"
git tag -a v0.0.20 "{pypi_version_link}"
git push origin v0.0.20
```

# このパッケージを更新(upload)する方法
## 共通
```sh
## pythonの環境を作成・接続
python3 -m venv venv
source venv/bin/activate
## アップロード用のパッケージインストール
pip install wheel twine
```
### pypiの本番環境にuploadする手順
```sh
# (必須)setup.cfgのバージョンを更新すること
rm dist/*
python setup.py bdist_wheel
twine upload --repository pypi dist/*
```
### test.pypiの開発環境にuploadする手順
```sh
## pypiへの準備・アップロード
python setup.py bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
- test.pypiからパッケージインストール
```sh
# ※ pip install時にパッケージが見つからないとエラーが出力された場合、
# ※ 個別にpip installしてから改めて自作パッケージをインストールする.
# ※ pip install -U PyMySQL
# バージョンを指定する必要がある.
# test.pypiのURL
# https://test.pypi.org/project/mo9mo9db/
pip install -i https://test.pypi.org/simple/ mo9mo9db
```
