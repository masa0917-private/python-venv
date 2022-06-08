# 仮想環境構築方法

1. カレントディレクトリでPYTHON-VENVに移動する
    (VScodeではPYTHON-VENVを開く)
2. 下記コマンドを実行
    python -m venv --without-pip <"Project Dir Name">
3. pipがインストールされていないのでインストールする
4. 下記コマンドを実行(仮想環境で)
    python get-pip.py
5. 念のため下記コマンドでpipを最新版にする
    python -m pip install --upgarade pip

以上で仮想環境プロジェクト構築完了