class StockSpanner:

    def __init__(self):
       self.stack = []
       self.count = 0 

    def next(self, price: int) -> int:
        self.count+=1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            ret = self.count - self.stack[-1][1] 
        else:
            ret = self.count
        self.stack.append([price, self.count])
        return ret 



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)