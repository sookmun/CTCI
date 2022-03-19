class AnimalShelter:

    def __init__(self):
        self.dogQueue=[]
        self.catQueue=[]
        self.numDog=0
        self.numCat=0
        self.timeStamp=0

    def enqueue(self,animal,type):
        if type=="C":
            self.catQueue.append((animal,self.timeStamp))
            self.numCat+=1
        else:
            self.dogQueue.append((animal,self.timeStamp))
            self.numDog+=1
        self.timeStamp+=1

    def dequeueAny(self):
        if self.catQueue[0][1]<self.dogQueue[0][1]:
            animal=self.catQueue.pop(0)
            self.numCat-=1
            return animal
        else:
            animal = self.dogQueue.pop(0)
            self.numDog -= 1
            return animal
    def dequeueDog(self):
        animal=self.dogQueue.pop(0)
        self.numDog -=1
        return animal

    def dequeueCat(self):
        animal=self.catQueue.pop(0)
        self.numCat -=1
        return animal

    def __str__(self):
        print("Dog: ",self.dogQueue)
        print("Cat: ",self.catQueue)
        return ">>>>"

if __name__ == '__main__':
    shelter=AnimalShelter()
    shelter.enqueue("bork","D")
    shelter.enqueue("demon", "C")
    shelter.enqueue("moon moon", "D")
    shelter.enqueue("stacy", "D")
    shelter.enqueue("tiger", "C")
    shelter.enqueue("ginger", "C")
    print(shelter)
    print(shelter.dequeueAny())
    # print(shelter.dequeueDog())
    print(shelter.dequeueCat())
    print(shelter.dequeueAny())
    print(shelter)
