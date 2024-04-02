from heuristik import calculate_h1
from paritaet import calculate_paritaet, is_possible
from board import possible_movements


def search_ids_deep(arr, limit):
    if limit == 0: return arr
    for i in possible_movements(arr):
        x = arr.copy()
        


def search_ids(arr):
    par = calculate_paritaet(arr)
    if is_possible(par) == False: return []

    return []

if __name__ == "__main__":
    field = [7, 2, 4, 5, 0, 6, 8, 3, 1] # Aufgabenstellung
    res = search_ids(field)
    print(res)
