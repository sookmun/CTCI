class Node:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

class BinaryTree:

    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.root is None

    def get_item(self,key):
        return self.get_item_aux(self.root,key)

    def get_item_aux(self,current,key):
        if current is None:
            return False
        elif key==current.key:
            return current
        elif key<current.key:
            return self.get_item_aux(current.left,key)
        else:
            return self.get_item_aux(current.right,key)

    def insert(self,key, item):
        self.insert_aux(self.root,key,item)

    def insert_aux(self,current,key,item):
        if current is None:
            current=Node(key,item)
            self.size+=1
        elif key<current.key:
            self.insert_aux(current,key,item)
        elif key>current.key:
            self.insert_aux(current, key, item)
        else:
            raise ValueError("Inserting Duplicate")

    def get_leaves(self):
        lst_leaves=[]
        self.get_leaves_aux(self.root,lst_leaves)
        return lst_leaves

    def get_leaves_aux(self,current,lst_leaves):
        if current is not None:
            if self.isLeaf(current):
                lst_leaves.append(current)
            else:
                self.get_leaves_aux(current.left,lst_leaves)
                self.get_leaves_aux(current.right, lst_leaves)

    def isLeaf(self,node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def pre_order(self):
        self.pre_order_aux(self.root)

    def pre_order_aux(self,current):
        if current is not None:
            print(current)
            self.pre_order_aux(current.left)
            self.pre_order_aux(current.right)

    def in_order(self):
        self.in_order_aux(self.root)

    def in_order_aux(self,current):
        if current is not None:
            self.in_order_aux(current.left)
            print(current)
            self.in_order_aux(current.right)

    def post_order(self):
        self.post_order_aux(self.root)

    def post_order_aux(self,current):
        if current is not None:
            self.post_order_aux(current.left)
            self.post_order_aux(current.right)
            print(current)

    def getHeight(self,current):
        if current is None:
            return 0
        else:
            left=self.getHeight(current.left)
            right = self.getHeight(current.right)
            return max(left,right) +1

