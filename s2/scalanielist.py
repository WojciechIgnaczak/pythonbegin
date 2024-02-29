lista=[1,2,6,7,3,4,8,9]
half=len(lista)//2
half1=lista[:half]
half2=lista[half:]
print(half1,half2)
newlist=[]
n=len(lista)
for i in range(n):
    if half1[0]<half2[0]:
        newlist.append(half1[0])
        half1.pop(0)
    else:
        newlist.append(half2[0])
        half2.pop(0)
    if len(half1)==0:
        for i in range(len(half2)):
            newlist.append(half2[i])
        break
    if len(half2)==0:
        for i in range(len(half1)):
            newlist.append(half1[i])
        break
print(newlist)