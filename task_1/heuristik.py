from board import calculate_distance

def calculate_h1(board: list[int]):
    res = 0
    for i in range(len(board)):
        cursor = board[i]
        if (cursor == 0 or cursor == i): continue
        res = res + 1
    return res

def calculate_h2(board: list[int]):
    res = 0
    for i in range(len(board)):
        cursor = board[i]
        if (cursor == 0): continue
        t = calculate_distance(cursor, i, board)
        res = res + t
    return res

if __name__ == "__main__":
    field = [7, 2, 4, 5, 0, 6, 8, 3, 1] # Aufgabenstellung

    res_h1 = calculate_h1(field)
    res_h2 = calculate_h2(field)
    print(res_h1, res_h2)