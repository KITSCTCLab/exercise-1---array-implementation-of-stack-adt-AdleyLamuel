class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top = -1

    def is_empty(self):
        if self.top == (self.size - 1) :
            return 1
        else :
            return 0

    def is_full(self):
        if self.top == -1 :
            return 1
        else :
            return 0

    def push(self, data):
        if not self.is_full():
            if self.isFull() !=1:
                self.top+=1
                self.items[self.top]=a

    def pop(self):
        if not self.is_empty():
            if self.isEmpty()!=1:
                t=self.items[self.top]
                del self.items[self.top]
                self.top-=1
                return t

    def status(self):
        if self.isEmpty()!=1:
            for i in range(0,self.top+1):
                print(self.items[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
