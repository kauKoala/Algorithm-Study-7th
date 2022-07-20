a,b=input().split()
a=int(a)
b=list(map(ord,b))
c=b


if a==1:
    print(''.join(map(chr,b)))

    for i in range(len(b)):
        if 96<b[i]<123:
            print(chr(b[i]),end='')
        else:
            print("_"+chr(b[i]+32),end='')
    print("")

    b[0]-=32
    print(''.join(map(chr,b)))

if a==2:
    for i in range(len(c)):
        if c[i]==95:
            c[i+1]-=32
        else:
            print(chr(c[i]),end='')
    print("")

  
    print(''.join(map(chr,b)))

    c[0]-=32
    print(''.join(map(chr,c)))

if a==3:
    c[0]+=32
    print(''.join(map(chr,c)))

    for i in range(len(c)):
        if 96<c[i]<123:
            print(chr(c[i]),end='')
        else:
            print("_"+chr(c[i]+32),end='')
    print("")
    print(''.join(map(chr,b)))


