# napisz funkcje ktora oblicza wysokosc drzewa binarnego. dlugosc drzewa jest najdłuższą ścieżką od korzenia do liścia

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def height(node):
    if node is None:
        return -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1
        
#DANE:
#         10
#     5       20
# 3         15   30

root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(3)
root.right.left=Node(15)
root.right.right=Node(30)
root.right.right.right=Node(30)
root.right.right.right.right=Node(30)
# root.right.right.right.right.right=Node(30)
#print("Wysokość :", height(root)) 

#sprawdx czy drzewo jest zbalansowane. jest zbalansowane jesli dla kazdefo wezla roznica wysokosci jego poddrzew lewego i 
#prawego nie przekracza 1
def balance(node):
    if node is None:
        return True
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        if abs(left_height-right_height)>1:
            return False
        else: 
            return balance(node.left) and balance(node.right)

#print(balance(root))


# wizualizacja efektu rotacji pojedynczej i podwojnej na drzewie binarnym. user podaje ciag operacji wstawiania, a nastepnie zobaczyc jak drzewo jest transformowane przez rotacje
#DANE:
#         10
#     5       20
# 3         15   30
def print_tree(node,level=0):
    if node is not None:
        if level == 0:
            print(" "*level*height(node)*2 + str(node.value))
            level+=1
        else:
            print_tree(node.left, level - 1)
            print_tree(node.right , level + 1)
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.right=Node(6)
root.right.left=Node(15)
root.right.right=Node(30)
print_tree(root)

#system rezerwacji samolotów jak drzewo binarne