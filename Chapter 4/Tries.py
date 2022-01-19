class Node:
    def __init__(self,data=None,level=None):
        self.data=data
        self.level=level
        self.links=[None]*27 #number of alphabets

class PrefixTrie:

    def __init__(self):
        self.root=Node()

    def insert(self,key):
        level=1
        current=self.root
        for letter in key:
            index= ord(letter) -97 +1
            if current.links[index] is not None:
                current.data+=1 #number of times node is visited
            else:
                current.links[index] = Node(level=level)
                current = current.links[index]
                current.data=1

            level+=1
        if current.links[0] is not None: #more than 1 same word
            current = current.links[0]
            current.data+=1
        else:
            current.links[0] = Node(level=level)
            current = current.links[0]
            # there is a word
            current.data = 1

    def search(self,key):
        current=self.root
        for alphabet in key :
            index=ord(alphabet)-97+1
            if current.links[index] is not None:
                current=current.links[index]
            else:
                return "not in trie"
        return True
if __name__ == '__main__':
    t=PrefixTrie()
    t.insert("happy")
    t.insert("sad")
    print(t.search("hap"))
    print(t.search("happy"))
    print(t.search("okay"))
