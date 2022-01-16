class myQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.count1=0
        self.count2=0

    def add(self,item):
        self.stack1.append(item)
        self.count1+=1

    def remove(self):
        print("count2",self.count2)
        if self.count2>0:
            print("hello")
            self.stack2.pop()
            self.count2-=1
        else:
            for item in range(self.count1-1):
                item=self.stack1.pop()
                self.count1-=1
                self.stack2.append(item)
                self.count2+=1
            self.count1-=1
            return self.stack1.pop()

if __name__ == '__main__':
    queue=myQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    print("stack1",queue.stack1)
    print("stack2",queue.stack2)
    print("itempop",queue.remove())
    queue.add(5)
    print("stack1", queue.stack1)
    print("stack2", queue.stack2)
    print("itempop",queue.remove())
    queue.remove()
    print("stack1", queue.stack1)
    print("stack2", queue.stack2)
    queue.remove()
    print("stack1", queue.stack1)
    print("stack2", queue.stack2)
    queue.remove()
    print("stack1", queue.stack1)
    print("stack2", queue.stack2)
