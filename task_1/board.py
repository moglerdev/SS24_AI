import math

def calculate_wh(board: list[int]):
    return math.sqrt(len(board))

def calculate_cords(i: int, wh: int):
    y = math.floor(i / wh)
    x = i - y * 3
    return (x, y)

def get_index(x: int, y: int, wh: int):
    t = wh * y
    return int(t + x)

def calculate_distance(a: int, b: int, board: list[int]):
    wh = calculate_wh(board)
    x1, y1 = calculate_cords(a, wh)
    x2, y2 = calculate_cords(b, wh)

    a2 = (x2 - x1) ** 2
    b2 = (y2 - y1) ** 2
    return math.ceil(math.sqrt(a2 + b2))

def find_zero(board: list[int]):
    for i in range(len(board)):
        if board[i] == 0: return i
    return -1

def move_board(i: int, board: list[int]):
    res = board.copy()
    z = find_zero(res)
    res[z] = res[i]
    res[i] = 0
    return res

def possible_movements(board: list[int]) -> list[int]:
    z = find_zero(board)
    wh = calculate_wh(board)
    x, y = calculate_cords(z, wh)
    res = []
    if x - 1 > -1: res.append(get_index(x - 1, y, wh))
    if x + 1 < wh: res.append(get_index(x + 1, y, wh))
    if y - 1 > -1: res.append(get_index(x, y - 1, wh))
    if y + 1 < wh: res.append(get_index(x, y + 1, wh))
    return res

def board_equals(a: list[int], b: list[int]) -> bool:
    for i in range(0, len(b)):
        if a[i] != b[i]: return False

    return True


def board_exist_in_path(board: list[int], path: list[list[int]]):
    for b in path:
        if board_equals(board, b): return True
    
    return False


if __name__ == "__main__":
    field = [1,2,3,4,0,5,6,7,8]
    # wh = calculate_wh(field)
    for p in possible_movements(field):
        print(p)

    x = get_index(1, 1, 3)
    print(x)

