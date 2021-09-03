def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    k = 0
    l = 0
    while k<n:
        i = float(input())
        l = l+i
        k = k+1
    s=(l/n)
    print(s)
if __name__=='__main__':
    main()
