🇺🇸 [README English Version](README_us.md)

🇰🇷 [README 한국어 버전](README.md)

# 🍎 リンゴゲームマクロ (Apple Game Macro)

MacBook Retinaディスプレイ用に作成された自動リンゴゲームマクロです。
[リンゴゲームリンク](https://www.gamesaien.com/game/fruit_box_a/)

> このプロジェクトは純粋に教育および学習目的で作成されました。実際のゲームでのマクロ使用はゲーム利用規約に違反する可能性があり、作成者はこれによる一切の責任を負いません。

## 🚀 インストール方法

1. Python仮想環境の作成と有効化

~~~zsh
python -m venv venv
source venv/bin/activate
~~~

2. 必要なパッケージのインストール

~~~zsh
pip install -r requirements.txt
~~~

## 🎮 実行方法
1. ゲーム画面を表示した状態で以下のコマンドでマクロを実行

~~~zsh
python apple_game_solver.py
~~~

## ✨ 主な機能

- 🔢 画面上の1-9までの数字（リンゴ）を自動認識
- 🎯 合計が10になる組み合わせを見つけて自動的にドラッグ
- 📏 水平/垂直ラインおよび四角形領域内の有効な組み合わせを探索
- 🖥️ Retinaディスプレイ解像度の自動補正
- 🔄 連続した2つ以上の数字の組み合わせを自動検出
- ➕ 四角形領域内の数字の合計計算

## ⚠️ 注意事項

- 💻 MacBook Retinaディスプレイに最適化
- 🔧 他の環境で使用する場合は座標値の調整が必要
- ⌨️ ゲーム実行中にマクロを終了するにはCtrl+C
- 🎯 実行前にゲーム画面がアクティブになっている必要があります
- ⏱️ 3秒間隔で新しいスキャンを実行
