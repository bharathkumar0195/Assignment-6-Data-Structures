"""Basic array, matrix, stack, queue and singly linked list operations."""
from collections import deque

class Array:
    def __init__(self, values=()): self.data = list(values)
    def access(self, i): return self.data[i]
    def insert(self, i, value): self.data.insert(i, value)
    def delete(self, i): return self.data.pop(i)

class Matrix:
    def __init__(self, rows):
        if rows and any(len(row) != len(rows[0]) for row in rows):
            raise ValueError('Rows must have equal lengths')
        self.rows = [list(row) for row in rows]
    def access(self, r, c): return self.rows[r][c]
    def update(self, r, c, value): self.rows[r][c] = value
    def insert_row(self, index, row):
        if self.rows and len(row) != len(self.rows[0]): raise ValueError('Wrong row width')
        self.rows.insert(index, list(row))
    def delete_row(self, index): return self.rows.pop(index)

class Stack:
    def __init__(self): self.data = []
    def push(self, value): self.data.append(value)
    def pop(self): return self.data.pop()
    def peek(self): return self.data[-1]
    def is_empty(self): return not self.data

class Queue:
    """Array-backed circular queue via deque (amortized O(1) append/popleft)."""
    def __init__(self): self.data = deque()
    def enqueue(self, value): self.data.append(value)
    def dequeue(self): return self.data.popleft()
    def front(self): return self.data[0]
    def is_empty(self): return not self.data

class Node:
    def __init__(self, value, next_node=None): self.value, self.next = value, next_node

class SinglyLinkedList:
    def __init__(self): self.head = None
    def insert_front(self, value): self.head = Node(value, self.head)
    def delete(self, value):
        previous, current = None, self.head
        while current:
            if current.value == value:
                if previous: previous.next = current.next
                else: self.head = current.next
                return True
            previous, current = current, current.next
        return False
    def traverse(self):
        result, node = [], self.head
        while node:
            result.append(node.value)
            node = node.next
        return result

if __name__ == '__main__':
    a = Array([1,3]); a.insert(1,2); assert a.data == [1,2,3]; assert a.delete(1)==2
    m = Matrix([[1,2],[3,4]]); m.update(0,1,8); assert m.access(0,1)==8
    s = Stack(); s.push(3); assert s.pop()==3
    q = Queue(); q.enqueue(5); assert q.dequeue()==5
    ll = SinglyLinkedList(); ll.insert_front(2); ll.insert_front(1); assert ll.traverse()==[1,2]; assert ll.delete(2)
    print('Data structure tests passed.')
