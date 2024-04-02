package task1

import "math"

func GetSize(board []int) int {
	l := len(board)
	return int(math.Sqrt(float64(l)))
}

func GetCords(index int, size int) (int, int) {
	y := index / size
	x := index - y*3
	return x, y
}

func GetIndexFromCords(x int, y int, size int) int {
	index := size * y
	return index + x
}

func GetDistance(a_index int, b_index int, board []int) float64 {
	size := GetSize(board)
	x1, y1 := GetCords(a_index, size)
	x2, y2 := GetCords(b_index, size)

	a2 := math.Pow(float64(x2-x1), 2)
	b2 := math.Pow(float64(y2-y1), 2)
	return math.Sqrt(a2 + b2)
}

func GetZeroIndex(board []int) int {
	for i, ele := range board {
		if ele == 0 {
			return i
		}
	}
	return -1
}

func MoveBoard(index int, board []int) []int {
	return []int{0}
}
