class Node:
    def __init__(self,id: int,name: str,date:str):
        self.id=id
        self.name=name
        self.date=date
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    
    def insert(self,id:int ,name:str,date:str):
        if self.root is None:
            self.root=Node(id,name,date)
        else:
            self._insert(self.root,id,name,date)
        
        
    def _insert(self,current_node:Node,id: int,name: str,date:str):
        if id < current_node.id:
            if current_node.left is None:
                current_node.left = Node(id, name, date)
            else:
                self._insert(current_node.left, id, name, date)
        elif id > current_node.id:
            if current_node.right is None:
                current_node.right = Node(id, name, date)
            else:
                self._insert(current_node.right, id, name,date)
        else:
            print("rezerwacja istnieje")
        
    def find(self,id):
        return self._find(self.root,id)
    
    def _find(self,current_node,id:int):
        if current_node:
            if current_node.id == id:
                return current_node
            if id < current_node.id:
                return self._find(current_node.left, id)
            return self._find(current_node.right, id)
        else:
            return None;
        
    def cancel(self,id):
        self.root=self._cancel(self.root,id)
        return id
    
    def _cancel(self,current_node,id):
        if current_node is None:
            return current_node
        if id<current_node.id:
            current_node.left=self._cancel(current_node.left,id)    
        elif id>current_node.id:
            current_node.right=self._cancel(current_node.right,id)    
        else:
            if current_node.left is None:
                temp=current_node.right
                current_node=None
                return temp
            elif current_node.right is None:
                temp=current_node.left
                current_node=None
                return temp
        temp=self.find_min(current_node.right)
        current_node.id=temp.id
        current_node.name=temp.name
        current_node.date=temp.date
        
        current_node.right=self._cancel(current_node.right,temp.id)  
        return current_node    
    
    def find_min(self,current_node):   
        while current_node.left:
            current_node = current_node.left
        return current_node
    
bst=BinarySearchTree()
bst.insert(1,'ala','2023-10-5')
bst.insert(12,'jan','2023-10-5')
bst.insert(11,'adam','2023-10-5')


found=bst.find(12)
if found:
    print(f'znaleziono {found.name,found.date}')
else: print("znaleziono nie ma")

deleted=bst.cancel(12)

print(f'ununieto {deleted}')


# def height(node):
#     if node is None:
#         return -1
#     else:
#         left_height = height(node.left)
#         right_height = height(node.right)
#         return max(left_height, right_height) + 1
# def print_tree(node,level=0):
#     if node is not None:
#         if level == 0:
#             print(" "*level*height(node)*2 + str(node.id))
#             level+=1
#         else:
#             print_tree(node.left, level - 1)
#             print_tree(node.right , level + 1)

# print_tree(bst)