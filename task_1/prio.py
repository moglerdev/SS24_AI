import heapq
from board import board_equals
from heuristik import calculate_h2

class AStarPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, heuristic_cost: int):
        heapq.heappush(self.heap, (heuristic_cost, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty priority queue")
        return self.heap[0][1]

    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def contains(self, item) -> bool:
        for _, element in self.heap:
            if board_equals(element, item):
                return True
        return False

    def get_priority(self, item) -> int:
        for priority, element in self.heap:
            if board_equals(element, item):
                return priority
        raise ValueError("Item not found in priority queue")

    def update_priority(self, item, new_priority: int):
        updated_heap = []
        for priority, element in self.heap:
            if board_equals(element, item):
                heapq.heappush(updated_heap, (new_priority, item))
            else:
                heapq.heappush(updated_heap, (priority, element))
        self.heap = updated_heap

    def __len__(self):
        return len(self.heap)
    
    def __str__(self):
        return ', '.join([str(item[1]) for item in self.heap])


# Example usage:
if __name__ == "__main__":
    pq = AStarPriorityQueue()
    pq.push("task1", 10)  # Beispiel: Priorität 5 + Heuristik 10 = 15
    pq.push("task2", 5)   # Beispiel: Priorität 1 + Heuristik 5 = 6
    pq.push("task3", 8)   # Beispiel: Priorität 3 + Heuristik 8 = 11

    print(pq)