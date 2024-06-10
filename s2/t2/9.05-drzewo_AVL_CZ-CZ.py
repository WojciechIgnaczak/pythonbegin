# drzewo AVL
# Rotacje- przemiszczenie węzłów

# 4 rodzaje rotacji- 2poj, 2podwojne

# rotacja prawo-prawo, lewo-lewo , celem jest zrownowazenie drzewa
# lewe dziecko zostanie usuniete


# rotacja RL, LR - najpierw ruch w prawo, a nastepnie całość tak jak LL,RR

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
        
def update_height(node):
    node.hight=max(height(node.left),height(node.right))+1
    
def height(node):
    if not node:
        return 0
    return node.height
        
def left_rotate(x):
    # 3                       2
    #     2       ->  1              2
    #         1
    y=x.right
    T2=y.left
    y.left=x
    x.right=T2
    update_height(x)
    update_height(y)
    return y

def right_rotate(y):
    
    #         3y
    #     2y.left           ->                      2y
    # 1y.left.left                       1y.left       3y.right
    x=y.left
    T2=x.right
    x.right=y
    y.left=T2
    update_height(x)
    update_height(y)
    return x

def right_left_rotate(node):
    node.right=right_rotate(node.right)
    return left_rotate(node)  

root=Node(30)
root.left=Node(20)
root.left.left=Node(10)

print(root.key)

root=right_rotate(root)
print(root.key)


#drzewo czerowno-czarne
https://eduinf.waw.pl/inf/alg/001_search/0121.php