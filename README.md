# 当リポジトリの自作パッケージを使うための準備
```py
pip install mo9mo9db
# https://pypi.org/project/mo9mo9db/
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

# pypiに新しいバージョンをuploadする簡易手順
```
# setup.cfgのバージョンを更新すること
python setup.py bdist_wheel
twine upload --repository pypi dist/*
```
