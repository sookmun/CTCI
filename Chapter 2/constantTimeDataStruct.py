import random
class DataStruct:

    def __init__(self):
        self.array=[]
        self.size=0
        self.hashTable={}

    def add(self,item):
        if self.hashTable.get(item) is None:
            self.array.append(item)
            self.size+=1
            self.hashTable[item]=self.size-1

    def remove(self,item):
        index= self.hashTable.get(item)
        if index is not None:
            self.hashTable.pop(item)
            self.size-=1
            last=self.array[-1]
            current=self.array[index]
            self.array[index],self.array[-1]=last,current
            self.hashTable[self.array[index]]=index
            self.array.pop()
        else:
            return "item not in list"

    def getRandom(self,):
        index=random.randrange(0,self.size)
        return self.array[index]

    def search(self,item):
        return self.hashTable.get(item)

    def __str__(self):
        print(self.array)
        print(self.size)
        print(self.hashTable)
        return ">>>"


if __name__ == '__main__':
    ds=DataStruct()
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    print(ds)
    # print(ds.search(30))
    ds.remove(20)
    print(ds)
    ds.add(50)
    print(ds)
    print(ds.search(50))
    print(ds.getRandom())

