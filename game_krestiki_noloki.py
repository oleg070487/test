# Функция для отображения игрового поля
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Функция для проверки выигрышной комбинации
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Функция для выполнения хода
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Эта клетка уже занята!")
        return False


# Основная функция игры
def tic_tac_toe():
    # Инициализация игрового поля
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    # Основной игровой цикл
    while True:
        display_board(board)
        row = int(input(f"Игрок {current_player}, выберите строку (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, выберите столбец (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Неверные координаты!")
            continue

        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                display_board(board)
                print(f"Игрок {current_player} выиграл!")
                break
            elif all(all(cell != " " for cell in row) for row in board):
                display_board(board)
                print("Ничья!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"


# Запуск игры
tic_tac_toe()