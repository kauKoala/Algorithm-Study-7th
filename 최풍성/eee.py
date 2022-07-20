n=int(input())
for i in range(n):
    a,b =input().split()
    x=list(a)
    y=list(b)
    arr=[]
    for j in range(len(x)):
        if x[j]<=y[j]:
            arr.append(ord(y[j])-ord(x[j]))
        else:
            arr.append(ord(y[j])-ord(x[j])+26)
    print("Distances: "+" ".join(map(str,arr)))