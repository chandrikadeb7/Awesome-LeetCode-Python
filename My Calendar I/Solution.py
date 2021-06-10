class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.cal, (start,end))
        if (i-1>=0 and self.cal[i-1][1]>start) or (i!=len(self.cal) and self.cal[i][0]<end):
            return False
        self.cal.insert(i,(start,end))
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
