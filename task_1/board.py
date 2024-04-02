import math

def calculate_wh(arr):
    return math.sqrt(len(arr))

def calculate_cords(i, wh):
    y = math.floor(i / wh)
    x = i - y * 3
    return (x, y)

def get_index(x, y, wh):
    t = wh * y
    return t + x

def calculate_distance(a, b, arr):
    wh = calculate_wh(arr)
    x1, y1 = calculate_cords(a, wh)
    x2, y2 = calculate_cords(b, wh)

    a2 = (x2 - x1) ** 2
    b2 = (y2 - y1) ** 2
    return math.ceil(math.sqrt(a2 + b2))

def find_zero(arr):
    for i in range(len(arr)):
        if arr[i] == 0: return i
    return -1

def move_board(i, arr):
    z = find_zero(arr)
    arr[z] = arr[i]
    arr[i] = 0
    return arr

def possible_movements(arr):
    z = find_zero(arr)
    wh = calculate_wh(arr)
    x, y = calculate_cords(z, wh)
    print(z, x, y, wh)
    res = []
    if x - 1 > -1: res.append((x - 1, y))
    if x + 1 < wh: res.append((x + 1, y))
    if y - 1 > -1: res.append((x, y - 1))
    if y + 1 < wh: res.append((x, y + 1))
    return res

if __name__ == "__main__":
    field = [1,2,3,4,0,5,6,7,8]
    wh = calculate_wh(field)
    for (x, y) in possible_movements(field):
        print(get_index(x, y, wh))

    x = get_index(1, 1, 3)
    print(x)