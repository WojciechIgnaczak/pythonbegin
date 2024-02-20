
a=7
b=21
def nwd(a,b):
    while a!=b:
        if a<b:
            b=b-a
        else:
            a=a-b
    return a
print(nwd(a,b))     

def nwd2(a,b):
    while b:
        a,b=b,a%b
    return print(a)
nwd2(48,12)