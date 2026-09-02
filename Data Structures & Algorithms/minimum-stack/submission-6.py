class MinStack:

    def __init__(self):
        self.stack = []
        self.last_entry = None
        self.least = None
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.last_entry = val
        if len(self.stack) == 1:
            self.min_stack.append(val)
            self.least = val
        elif len(self.stack) > 1:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
            self.least = self.min_stack[-1]

    def pop(self) -> None:
        val = self.stack.pop()
        if self.stack:
            self.last_entry = self.stack[-1]
        else:
            self.last_entry = None
        self.min_stack.pop()
        if self.min_stack:
            self.least = self.min_stack[-1]
        else:
            self.least = None
        

    def top(self) -> int:
        return self.last_entry
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
