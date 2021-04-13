class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        stack = nestedList
        
        while stack:
            k = stack[0]
            stack  = stack[1:]
            if k.isInteger():
                self.res.append(k)
            else:
                stack=k.getList()+stack
                
        self.i=0
        
    def next(self) -> int:
        self.i+=1
        return self.res[self.i-1]   
    
    def hasNext(self) -> bool:
        return self.i < len(self.res)
