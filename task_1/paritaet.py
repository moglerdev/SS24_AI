

def calculate_paritaet(board: list[int]):
    res = []
    for y in range(len(board)):
        cursor = board[y]
        if (cursor == 0): continue
        for x in range(y):
            shouldBeSmaller = board[x]
            if shouldBeSmaller == 0: continue
            if shouldBeSmaller > cursor:
                res.append((cursor, shouldBeSmaller))
    return res

def is_possible(par):
    return len(par) % 2 == 0

if __name__ == "__main__":
    field = [7, 2, 4, 5, 0, 6, 8, 3, 1] # Aufgabenstellung
    # # field = [1, 4, 2, 6, 7, 8, 3, 5] # Wikipedisa

    par = calculate_paritaet(field)
    print(par)

    print("Parität: ", "gerade => lösbar" if len(par) % 2 == 0 else "ungerade => nicht lösbar", " (", len(par), ")")
