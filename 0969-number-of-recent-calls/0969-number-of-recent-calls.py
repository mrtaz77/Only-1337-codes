class RecentCounter:

    def __init__(self):
        self.tail = self.head = -1
        self.queue = []
    
    def length(self) -> int:
        return self.head - self.tail + 1

    def ping(self, t: int) -> int:
        if len(self.queue) == 0:
            self.tail = self.head = 0
            self.queue.append(t)
        else:
            self.queue.append(t)
            self.head += 1
            while self.queue[self.head] - self.queue[self.tail] > 3000:
                self.tail += 1
        return self.length()
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)