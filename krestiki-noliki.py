def print_board(board):
    print("\n  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {'|'.join(row)}")
        if i < 2:
            print("  -+-+-")

def get_move(board, player):
    while True:
        try:
            move = input(f"Ходит игрок {player},впишите строку и столбец(пример: 0 0): ")
            row, col = map(int, move.split())
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Ошибка! Числа должны быть от 0 до 2")
                continue
                
            if board[row][col] != " ":
                print("Эта клетка уже занята!")
                continue

            return row, col
        
        except:
            print("Ошибка ввода!")

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def show_result(winner):
    print("\n" + "="*30)
    if winner == "Ничья":
        print("Ничья!")
    else:
        print(f"Победил игрок {winner}!")
    print("="*30)

def play_game():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    current_player = "X"
    moves = 0
    
    print("\n" + "="*30)
    print("<<< Крестики-нолики >>>")
    print("="*30)
    print("Вводите два числа через пробел")
    print("Первое - строка (0-2), второе - столбец (0-2)")
    print("="*30)
    
    while True:
        print_board(board)
        
        row, col = get_move(board, current_player)
        
        board[row][col] = current_player
        moves += 1
        
        if check_win(board, current_player):
            print_board(board)
            show_result(current_player)
            break
        
        if moves == 9:
            print_board(board)
            show_result("Ничья")
            break
        
        current_player = "O" if current_player == "X" else "X"

def main():
    print("Добро пожаловать в Крестики-нолики!")
    
    while True:
        play_game()
        
        while True:
            answer = input("\nСыграть еще? (да/нет): ").lower()
            if answer in ["да","yes"]:
                break
            elif answer in ["нет","no"]:
                print("Спасибо за игру!")
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'")

if __name__ == "__main__":
    main()