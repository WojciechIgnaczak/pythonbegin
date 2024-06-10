# zaimplementuj klase hashtable ktora bedzie dzialac jako slownik.
# put(key,value)-dodaje do tablicy
# get(key)-zwraca wartpsc
# remove(key)-usuwa po kluczu

class HashTable:
    def __init__(self,size=100):
        self.size=size
        self.table=[[]for _ in range(size)]
    def display(self):
        for i,bucket in enumerate(self.table):
            if bucket:
                print(f"Index: {i}: {bucket}")
            else:
                print(f"Index: {i}: Empty")
    def _hash(self,key):
        return hash(key)%self.size
    
    def put(self,key,value):
        index=self._hash(key)
        for kv in self.table[index]:
            if kv[0]==key:
                kv[1]=value
                return
        self.table[index].append([key,value])
    
    def get(self,key):
        index=self._hash(key)
        for kv in self.table[index]:
            if kv[0]==key:
                return kv[1]
        return None
    
    def remove(self,key):
        index=self._hash(key)
        for i,kv in enumerate(self.table[index]):
            if kv[0]==key:
                del self.table[index][i]
                return 
            
# ht=HashTable()
# ht.put("apple",1)
# ht.put("banana",2)
# ht.remove('banana')
# ht.display()





#metoda otwartego adresowania
class OpenAdressinghashTable:
    def __init__(self,size=100):
        self.size=size
        self.table=[None]*size
        
    def _hash(self,key):
        return hash(key)%self.size
    
    def _next(self,index):
        return (index+1)% self.size
    
    def put(self,key,value):
        index=self._hash(key)
        while self.table[index] and self.table[index][0]!=key:
            index=self._next(index)
        self.table[index]=(key,value)
        
    def get(self,key):
        index=self._hash(key)
        while self.table[index]:
            if self.table[index][0]==key:
                return self.table[index][1]
            index=self._next(index)
        return None
            
    def display(self):
        for i,kv in enumerate(self.table):
            if kv is not None:
                print(f"Index: {i}: {kv}")
            else:
                print(f"Index: {i}: Empty")
add=OpenAdressinghashTable()
add.put("banana",2)
add.put("apple",1)
add.display()





    
