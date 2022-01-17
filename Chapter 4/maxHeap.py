#array implementation
#children of k= 2*k and 2*k+1
#parent of k = k//2 (except root)

class Heap:

    def __init__(self,maxSize):
        self.count=0
        self.array=[None] *maxSize+1 #offset cuz start at 1

    def __len__(self):
        return self.count

    def is_full(self):
        return self.count+1 == len(self.array)

    def rise(self,k):
        while k> 1 and self.array[k] > self.array[k//2]:
            self.swap(k,k//2)
            k=k//2
    def swap(self,a,b):
        self.array[a],self.array[b]=self.array[b],self.array[a]

    def add(self,element):
        if not self.is_full():
            self.count+=1
            self.array[self.count]=element
            self.rise(self.count)

    def largest_child(self,k):
        if 2*k == self.count or self.array[2*k] > self.array[2*k+1]:
            return 2*k
        else:
            return 2*k+1

    def sink(self,k):
        while 2*k <= self.count:
            child = self.largest_child(k)
            if self.array[k] >= self.array[child]:
                break
            self.swap(child,k)
            k=child

