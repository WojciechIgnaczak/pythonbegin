import sys
a=11
def czy_pierwsza(a):
    for i in range(2,a):
        if a%i==0:
            print("nie jest pierwsza")
            sys.exit()
    print("liczba jest pierwsza")

czy_pierwsza(a)