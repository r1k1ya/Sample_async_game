# Tic-Tac-Toe Online (〇×ゲーム)

このリポジトリは、Pythonで作成したオンライン対戦型の〇×ゲーム（Tic-Tac-Toe）です。
サーバーとクライアントで構成され、2人のプレイヤーが対戦できます。

## 🚀 機能一覧
- 〇×ゲームの基本ルールに対応
- サーバーとクライアント間の通信に **ソケット通信** を使用
- **Tkinterを使ったGUI** により、直感的な操作が可能
- 先攻・後攻（`X` / `O`）が自動で決まる
- 勝敗判定機能付き

## 🛠️ 必要な環境
- `Python 3.8` 以上
- `asyncio`, `socket`, `tkinter`（標準ライブラリのため追加インストール不要）

## 📥 インストール & 実行方法
### 1. リポジトリをクローン
```bash
git clone https://github.com/r1k1ya/Sample_async_game.git
cd Sample_async_game
```

### 2. サーバーを起動
```bash
python oxgame_server.py
```

### 3. クライアントを起動（別のターミナルで実行）
```bash
python oxgame_client.py
```

※ 2つのクライアントを起動すると、対戦が可能になります。

## 🎮 遊び方
1. サーバーを起動し、プレイヤー2人がそれぞれクライアントを起動します。
2. 先攻・後攻が自動で割り当てられ、プレイヤーごとに **`X` / `O`** が決まります。
3. 交互にマス目をクリックし、縦・横・斜めのいずれかで3つ並べたプレイヤーが勝利！
4. 勝敗が決まると、ウィンドウタイトルに **勝者が表示** されます。

## 📜 ライセンス
このプロジェクトは **MITライセンス** のもとで公開されています。

## ✨ 貢献
バグの報告や機能追加の提案があれば、`Issue` や `Pull Request` をお願いします！


