import asyncio
import tkinter as tk
import socket
import threading

class TicTacToeClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Connecting...")
        
        self.buttons = []
        self.board = [" "] * 9
        self.current_turn = "X"
        self.player_symbol = None
        self.running = True

        self.create_ui()
        threading.Thread(target=self.start_client, daemon=True).start()

    def create_ui(self):
        for i in range(9):
            btn = tk.Button(self.root, text=" ", font=("Arial", 20), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == " " and self.current_turn == self.player_symbol:
            self.send_move(index)

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])
        self.root.title(f"Tic Tac Toe - {self.player_symbol} (Your Turn: {self.current_turn})")

    def send_move(self, move):
        if self.socket:
            self.socket.sendall(f"{move}\n".encode())

    def start_client(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 8888))
        self.player_symbol = self.socket.recv(2).decode().strip()
        self.root.title(f"Tic Tac Toe - You are {self.player_symbol}")

        while self.running:
            data = self.socket.recv(1024).decode().strip()
            print(f"Received: {data}")  # 受信データのデバッグ用

            if not data:
                break

            if "Game Over" in data:
                _, winner = data.split(",")
                self.root.title(f"Game Over! Winner: {winner}")
                self.running = False
                break

            parts = data.split(",")

            if len(parts) != 10:
                print(f"Error: Invalid data received ({len(parts)} elements) - {data}")
                continue

            *self.board, self.current_turn = parts
            self.board = [cell.replace("_", " ") for cell in self.board]  # "_" を " " に戻す
            self.update_board()

        self.socket.close()

# GUI起動
root = tk.Tk()
client = TicTacToeClient(root)
root.mainloop()
