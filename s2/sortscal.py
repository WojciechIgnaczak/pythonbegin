list=[1,2,5,4,3,6,7,8]
n=len(list)//2
new1=list[0:n]
new2=list[n:]
new_list=[]
for i in range(0,n-1):
    if new1[0]<new2[0]:
        new_list.append(new1[0])
        new1.pop(0)
    else:
        new_list.append(new2[0])
        new2.pop(0)
if len(new1)==1:
    new_list.append(new1[0])
    new1.pop(0)
else:
    new_list.append(new2[0])
    new2.pop(0) 
            
print(new_list)

#zrob sortowanie przez scalanie