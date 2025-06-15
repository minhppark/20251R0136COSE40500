class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        print(f"Pushing {item} onto stack")
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        item = self.stack.pop()
        print(f"Popping {item} from stack")
        return item

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return not self.stack

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        print(f"Enqueue {item}")
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue.pop(0)
        print(f"Dequeue {item}")
        return item

    def is_empty(self):
        return not self.queue

if __name__ == "__main__":
    s = Stack()
    for i in range(3):
        s.push(i)
    s.pop()
    s.pop()

    q = Queue()
    for i in range(3):
        q.enqueue(i)
    q.dequeue()
    q.dequeue()