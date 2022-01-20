class Node:
    def __init__(self,data=None,level=None):
        self.data=data
        self.links=[None]*27
        self.level=level

class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self,word):
        current=self.root
        for alphabet in word:

            index = ord(alphabet)-96
            if current.links[index] is not None:

                current=current.links[index]
            else:

                current.links[index]=Node()
                current=current.links[index]

        if current.links[0] is not None:
            current=current.links[0]
            current.data+=1
        else:
            current.links[0]=Node
            current=current.links[0]
            current.data=1

    def search(self,word):
        current=self.root
        for alphabet in word:

            index=ord(alphabet)-96
            if current.links[index] is not None:
                current=current.links[index]
            else:
                return 0
        if current.links[0] is not None:
            current=current.links[0]
            return current.data
        else:
            return 0



def wordFreq():
    t=Trie()
    t.insert("happy")
    t.insert("sad")
    t.insert("happy")
    print(t.search("happy"))

if __name__ == '__main__':
    wordFreq()