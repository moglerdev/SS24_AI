from heuristik import calculate_h1
from paritaet import calculate_paritaet, is_possible
from board import possible_movements, move_board, get_index, calculate_wh, board_exist_in_path

def search_ids_deep(board: list[int], path: list[list[int]], limit: int):
    nextPath = path.copy()
    nextPath.append(board)
    if (calculate_h1(board) == 0): return True, nextPath
    if limit == 0: return False, nextPath
    for a in possible_movements(board): # Problem, recrusion
        next = move_board(a, board)
        if board_exist_in_path(next, nextPath):
            continue
        found, foundedPath = search_ids_deep(next, nextPath, limit=limit-1)
        if found: return True, foundedPath

    return False, path

def search_ids(board: list):
    par = calculate_paritaet(board)
    if is_possible(par) == False: return []
    for limit in range(5, 100, 1):
        print("limit="+str(limit))
        founded, path = search_ids_deep(board, [], limit)
        if founded: return path
    return []

if __name__ == "__main__":
    field = [7, 2, 4, 5, 0, 6, 8, 3, 1] # Aufgabenstellung
    # field = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9] # limit == 1
    res = search_ids(field)
    print(len(res) - 1)
    for board in res:
        for i in range(0, 9, 3):
            print(board[i:i+3])
        print()
