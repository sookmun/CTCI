lst=[0]*15
class Pointer:

    def __init__(self,boundary,maxSize):
        self.boundary=boundary
        self.maxSize=maxSize
        self.size=0
        self.current=boundary-1

    def push(self,item):
        if self.size<self.maxSize:
            lst[self.current]=item
            self.current+=1
            self.size+=1
        else:
            return "stack is full"
    def pop(self):
        print("current",self.current)
        if self.current>=self.boundary and self.current<self.boundary+5:
            item=lst[self.current]
            lst[self.current]=0
            self.size-=1
            self.current-=1
            return item
        else:
            return "out of bounds"



def question1():
    # lst=[0]*15
    stack1=Pointer(0,5)
    stack2=Pointer(5,5)
    stack3=Pointer(11,5)
    #pushing someting into stack 1
    stack1.push(1)
    stack1.push(1)
    stack1.push(1)
    stack1.push(1)
    print(lst)
    print(stack1.current)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    print(stack1.pop())
    print(stack1.pop())
    print(lst)

if __name__ == '__main__':
    question1()