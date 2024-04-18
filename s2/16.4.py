# DRZEWO
# to odwrocone drzewo ktore nasladuje odwrocona forme drzewa- hierarchia
# jezeli kazdy rodzic ma jedno dziecko to drzewo to lista
# drzewa przechowywane :
#     bezposrednie odniesienie do wezlow
class Node:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right = None 

#    lista dzieci
class Node:
    def __init__(self,data):
        self.data =data
        self.children=[]
    
#drzewa binarne - drzewa dwuelementowe, kazdy rodzic ma 2 dzieci
#indeksy-[0,1,2,3,4,5,6]
tree=[1,2,3,4,5,6,7]

def get_left_child(index):
    return 2*index+1
def get_right_child(index):
    return 2*index+2
def get_parent(index):
    return (index-1)//2
# distep do elementow drzewa
index=0 #korzen
left_child_index=get_left_child(index)
right_child_index=get_right_child(index)
# print(f"wartosc korzen: {tree[index]}")
# print(f"wartosc lewe dziecko korzenia: {tree[left_child_index]}")
# print(f"wartosc prawe dziecko korzenia: {tree[right_child_index]}")


# Odnosnik rodzic dziecko
class Node:
    def __init__(self,data):
        self.data =data
        self.parent=None
        self.children = []

# rekurencyjne struktury danych- drzewo mozna traktowac rekurencyjnie, gdzie kazde poddrzewo jest instancja calego drzewa
#drzewa AVL, czerwono-czarne
# BINARNE- kazdy dziecko zawiera dane to prawego, lewego dziecka,czasem do rodzica. Do sortowania, wyszukiwania binarnego, w systemach zarzadzania baza danych i algorytmach grafowych,kopce binarne
# Drzewo binarne poszukiwań BST - dla kazdego wezla wszystkie elementy w lewym poddrzewie są wieksze od wezla a w prawym wieksze od wezla
#zbalansowane drzewo
# pełne drzewo binarne - kazdy wezel ma 2 dzieci
# kompleten drzewo binarne
# doskonałe drzewo binarne -kazdy wezel ma 2 dzieci a liscie na tym samym poziomie

# Przeglądanie węzłów drzewa- odwiedzanie kazdego wezla dokladnie raz

# Przeszukiwanie w głąb DFS
# pre-order -korzen-lewe-prawe
# in-order lewe-korzen-prawe do sortowania
# post-order lewe-prawe-korzen do kasowania całego drzewa
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
def dfs_preorder(node):
    if node:
        print(node.value)
        dfs_preorder(node.left)
        dfs_preorder(node.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Przeszukiwanie w gląb DFS")
dfs_preorder(root)
    #     1
    #     /\
    #    2   3
    #  /  \
    # 4     5
    
    
# PRZESZUKIWANIE W SZZERZ BFS od korzenia i przechodzi do wszystkich węzłów

from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def bfs(root):
    queue=deque([root])
    while queue:
        current= queue.popleft()
        print(current.value)
        
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)
print("Przeszukiwanie w gląb BFS")
bfs(root)


# Gdzie drzewa i algorytmy przeszukiwania: 1. Bazy danych, 2. Systemy plików, 3.Algorytmy sztucznej inteligencji, grafika komp, algorytmy przeszukiwania sciezek, struktury danych,kompilatory,analiza danych
# Przeszukiwanie liniowe i binarne. drzewa przeszukiwan binarnych
# Liniowe i binarne to 2 podstawowe zasady sprawdzania np. iteracja listy. Prosta imoplementacja, nie trzeba sortowania, niska efektywnosc dla duzych zbiorow danych
# przeszukiwanie binarne- wymaga posortowanych danych wejsciowych, dzieli na połowy, wybierając środkowy i porównuje o z szukanym elementem. proces jest powtarzany dla odpowiedniej polowy zakresu
# wysoka efektywnosc, szybsze niz liniowe dl aduzych zbiorów, wymaga sortowania, nieefektywne dla małych zbiorów

def binarysearch(arr,target)

# drzewo przeszukiwan binarnych.
