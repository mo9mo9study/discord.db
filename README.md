```
ddl/
    master/create_table.sql : DDL文。これをDBに流し込めば本番環境と同じ状態になるよう保つ。
    patch/ : TBD。migrationの仕組みが導入されるまで、DBスキーマ変更用DDLはここに置く。レビュー完了後masterのDDLにも反映する。
ERD/
    draw.ioで書かれたERD
```
# Future
- 今後は当リポジトリで記載しているファイル群をpipでインストールできる様にする
- 今後pep8に準拠した書式で記載する


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

# 当リポジトリのファイルを事項するための準備
## 環境はvenvにて作成しています
## 実行に必要なパッケージはrequirements.txtに記載しています
```py
# pythonの仮想環境を作成する
python3 -m venv venv
# 仮想環境にアタッチする
source venv/bin/activate
# 必要なパッケージを仮想環境ないでインストールする
pip3 install -r requirements.txt
```
