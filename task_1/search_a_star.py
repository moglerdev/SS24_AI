from heuristik import calculate_h2
from paritaet import calculate_paritaet, is_possible
from board import possible_movements, move_board, get_index, calculate_wh, board_exist_in_path
from prio import AStarPriorityQueue

pred = {}
costs = {}

def search_a_star_deep(start: list[int]):
    openList = AStarPriorityQueue()

    cost = calculate_h2(start)
    openList.push(start, cost)
    pred[tuple(start)] = None
    costs[tuple(start)] = 0
    
    while not openList.is_empty():
        current = openList.pop()
        h2 = calculate_h2(current)
        if h2 == 0: return construct_path(current)

        for i in possible_movements(current):
            neighbor = move_board(i, current)
            cost_current = costs[tuple(current)]
            if not openList.contains(neighbor) and tuple(neighbor) not in pred:
                costs[tuple(neighbor)] = cost_current + 1
                pred[tuple(neighbor)] = current
                openList.push(neighbor, costs[tuple(neighbor)] + calculate_h2(neighbor))
            elif openList.contains(neighbor):
                if cost_current + 1 < costs[tuple(neighbor)]:
                    costs[tuple(neighbor)] = cost_current + 1
                    pred[tuple(neighbor)] = current
                    openList.push(neighbor, costs[tuple(neighbor)] + calculate_h2(neighbor))
    return None

def construct_path(node):
    path = []
    while node:
        path.append(node)
        node = pred.get(tuple(node))
    return path[::-1]

if __name__ == "__main__":
    field = [7, 2, 4, 5, 0, 6, 8, 3, 1] # Aufgabenstellung
    # field = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9] # limit == 1
    res = search_a_star_deep(field)
    print(len(res) - 1)
    for board in res:
        for i in range(0, 9, 3):
            print(board[i:i+3])
        print()
