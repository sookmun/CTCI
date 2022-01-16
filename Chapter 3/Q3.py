#implementation not tested yet
#also very hacky way
class SetofStacks:
    def __init__(self):
        self.sets=[]

class Stack():
    def __init__(self):
        self.setOfStacks=[]
        self.stack=[]
        self.threshold=5
        self.count=0
    def pop(self):
        return self.stack.pop()

    def creatNew(self,item):
        self.setOfStacks.append(self.stack)
        self.stack=[item]

    def push(self,item):
        if self.count<=self.threshold:
            self.stack.append(item)
            self.count+=1
        else:
            self.creatNew(item)
    def popAt(self,index):
        assert index < len(self.setOfStacks),"index out of bounds"
        if index==len(self.setOfStacks)+1:
            self.stack.pop()
        else:
            current=self.setOfStacks[index]
            current.pop()



