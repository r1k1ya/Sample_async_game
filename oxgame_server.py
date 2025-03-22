import asyncio

# ゲームの状態を管理
board = [" "] * 9
current_turn = "X"
players = []

# 勝敗判定
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦
        [0, 4, 8], [2, 4, 6]  # 斜め
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return "Draw" if " " not in board else None

# クライアントの処理
async def handle_client(reader, writer):
    global current_turn
    addr = writer.get_extra_info('peername')
    print(f"Player connected: {addr}")

    players.append(writer)
    player_symbol = "X" if len(players) == 1 else "O"

    writer.write(player_symbol.encode() + b"\n")  # プレイヤーの記号を送信
    await writer.drain()

    while True:
        # " "（スペース）を "_" に置き換えて送信
        board_state = ",".join(board).replace(" ", "_") + f",{current_turn}"
        print(f"Sending: {board_state}")  # デバッグ用
        writer.write(board_state.encode() + b"\n")
        await writer.drain()

        if player_symbol != current_turn:
            await asyncio.sleep(1)
            continue

        data = await reader.readline()
        if not data:
            break

        try:
            move = int(data.decode().strip())
            if 0 <= move < 9 and board[move] == " ":
                board[move] = current_turn
                winner = check_winner()
                if winner:
                    for p in players:
                        p.write(f"Game Over,{winner}".encode() + b"\n")
                        await p.drain()
                    break
                current_turn = "O" if current_turn == "X" else "X"
        except ValueError:
            pass

    writer.close()
    await writer.wait_closed()


# サーバー起動
async def start_server():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print("Server started on 127.0.0.1:8888")
    async with server:
        await server.serve_forever()

asyncio.run(start_server())

