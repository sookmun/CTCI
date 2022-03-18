class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def append(self,node,current):
        current.next=node
        self.size+=1

    def isempty(self):
        if self.size==0:
            return True
        else:
            return False

    def getNode(self,index):
        assert 0 <= index <self.size, "Index out of Bounds"
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def __len__(self):
        return self.size

    def __str__(self):
        current=self.head
        retstr=""
        while current.next != None:
            retstr+="->"+str(current.data)
            current=current.next
        retstr+="->" +str(current.data)
        return retstr
    #answer to question 2.3
    def delete(self,node):
        current=self.head
        prev=None
        while current!=None:
            if current.data==node.data:
                if prev==None:
                    self.head=current.next
                else:
                    prev.next=current.next
            prev=current
            current=current.next

def test():
    k=[1,2,3,4,5,6,7]
    lst=LinkedList()
    head=Node(k[0])
    lst.head=head
    current=head
    for index in range(1,len(k)):
        node=Node(k[index])
        lst.append(node,current)
        current=node
    print(lst)
    node=Node(1)
    lst.delete(node)
    print(lst)

def palindrome(lst):
    stack=[]
    current=lst.head
    while current is not None:
        stack.append(current.data)
        current=current.next
    current = lst.head
    for i in range(len(stack)):
        item=stack.pop()
        if current.data != item:
            return False
        current=current.next
    return True
def kLast(k,lst): #question 2.2
    #because i have a counter for size, index= size-k
    kth=lst.size-k+1
    current=lst.head
    for index in range(kth):
        current=current.next
    return current

def question1(lst): #question 2.1
    repeats={}
    current=lst.head
    prev=None
    print(lst)
    while current is not None:
        if repeats.get(current.data) is None:
            repeats[current.data]=1

        else:
            prev.next=current.next
            print(current.data)

        prev = current
        current=current.next
        # print(current)
    print(lst)

if __name__ == '__main__':
    # test()
    # k = [1, 2, 3, 4,  4,5, 6,3,1, 7]
    # lst = LinkedList()
    # head = Node(k[0])
    # lst.head = head
    # current = head
    # for index in range(1,len(k)):
    #     node=Node(k[index])
    #     lst.append(node,current)
    #     current=node
    # # print(kLast(3,lst))
    # question1(lst)
    #for palindrome
    k = [1, 2,2,3,0,3,2,2,1]
    lst = LinkedList()
    head = Node(k[0])
    lst.head = head
    current = head
    for index in range(1, len(k)):
        node = Node(k[index])
        lst.append(node, current)
        current = node
    print(palindrome(lst))
