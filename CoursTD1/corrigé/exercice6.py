# Exercise 2: Build stack and queue using OOP

class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def __str__(self) -> str:
        return str(self.stack)

    def get_size(self):
        return len(self.stack)

    def push(self, value: list | int):
        if isinstance(value, int):
            self.stack = [value, *self.stack]
        else:
            self.stack = [*list(reversed(value)), *self.stack]

    def pop(self):
        popped_value = self.stack[0]
        self.stack = self.stack[1:]
        return popped_value


class Queue():
    def __init__(self) -> None:
        self.queue_ = []

    def __str__(self) -> str:
        return str(self.queue_)

    def get_size(self):
        return len(self.queue_)

    def enqueue(self, value: list | int):
        if isinstance(value, int):
            self.queue_ = [*self.queue_, value]
        else:
            self.queue_ = [*self.queue_, *value]

    def dequeue(self):
        popped_value = self.queue_[0]
        self.queue_ = self.queue_[1:]
        return popped_value


if __name__ == "__main__":
    # Create stack and test implemented methods
    print("Stack")
    stack = Stack()
    print(stack)
    stack.push(value=1)
    stack.push(value=[2,3,4])
    print(stack)
    popped_value = stack.pop()
    print(popped_value)
    print(stack)

    # Create queue and test implemented methods
    print("\nQueue")
    queue_ = Queue()
    print(queue_)
    queue_.enqueue(value=1)
    queue_.enqueue(value=[2,3,4])
    print(queue_)
    popped_value = queue_.dequeue()
    print(popped_value)
    print(queue_)
