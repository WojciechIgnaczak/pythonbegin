a=65977
def dzielniki(a):
    dzielnik=[]
    for i in range(1,a+1):
        if a%i==0:
            dzielnik.append(i)
    return print(dzielnik)
dzielniki(a)