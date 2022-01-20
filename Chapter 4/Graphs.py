class Node:
    def __init__(self,data):
        self.data=data
        self.adjacent=[]
        self.visited=False

    def __str__(self):
        print(self.data)
        # for node in self.adjacent:
        #     print(node.data)
        return ""

class Graph:
    def __init__(self):
        self.nodes=[]

    def insert(self,current):
        self.nodes.append(current)

    def join(self,current,newNode):
        current.adjacent.append(newNode)

    def __str__(self):
        for node in self.nodes:
            print(node)
        return ""

    def dfs(self,root):
        if root==None:
            return
        print(root.data)
        root.visited=True
        for node in root.adjacent:
            if not node.visited:
                self.dfs(node)

    def bfs(self,node):

        queue=[]
        queue.append(node)
        node.visited=True
        while len(queue)>0:
            current=queue.pop(0)
            # print("queue",queue)
            print(current,end="=>")
            for adjacent in current.adjacent:
                if adjacent.visited==False:
                    # print("data",adjacent.data)
                    adjacent.visited = True
                    queue.append(adjacent)







if __name__ == '__main__':
    g=Graph()
    o=Node(1)
    t=Node(2)
    th=Node(3)
    f=Node(4)
    fi=Node(5)

    g.insert(o)
    g.join(o, t)
    g.join(o, th)
    g.join(o, f)
    g.insert(t)
    g.join(t, o)
    g.join(t, th)
    g.join(t, fi)

    g.insert(th)
    g.join(th, o)
    g.join(th, t)
    g.join(th, fi)

    g.insert(f)
    g.join(f, o)
    g.join(f, fi)
    g.insert(fi)
    g.join(fi, t)
    g.join(fi, th)
    g.join(fi, f)
    # print(g)
    # g.dfs(th)
    g.bfs(th)