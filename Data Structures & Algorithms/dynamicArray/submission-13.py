class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []


    def get(self, i: int) -> int:
        return self.array[i]



    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        curr_size = self.getSize()
        if curr_size == self.capacity:
            self.resize()
        if n in self.array:
            self.array[self.array.index(n)] = None
        self.array.append(n)


    def popback(self) -> int:
        return self.array.pop()
 

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        sum = 0
        for item in self.array:
            sum += 1
        return sum
        
    
    def getCapacity(self) -> int:
        return self.capacity
