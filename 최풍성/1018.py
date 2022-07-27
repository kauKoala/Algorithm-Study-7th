n,m=map(int,input().split())
arr=[]
for i in range(n):
    s=list(input())
    arr.append(s)
ans=[0]*(n-7)*(m-7)
for i in range(n-7):
    for j in range(m-7):
        test = []
        for k in range(8):
           test.append(arr[i+k][j:8+j])
        if test[0][0]=="B":
           for q in range(8):
            if q%2==0:
                for x in range(4):
                    if test[q][2*x+1]=="B":
                        ans[(m-7)*i+j]+=1
                for x in range(4):
                    if test[q][2*x]=="W":
                        ans[(m-7)*i+j]+=1
            else:
                for x in range(4):
                    if test[q][2*x]=="B":
                        ans[(m-7)*i+j]+=1
                for x in range(4):
                    if test[q][2*x+1]=="W":
                        ans[(m-7)*i+j]+=1      
        else:
           for q in range(8):
            if q%2==0:
                for x in range(4):
                    if test[q][2*x+1]=="W":
                        ans[(m-7)*i+j]+=1
                for x in range(4):
                    if test[q][2*x]=="B":
                        ans[(m-7)*i+j]+=1
            else:
                for x in range(4):
                    if test[q][2*x]=="W":
                        ans[(m-7)*i+j]+=1
                for x in range(4):
                    if test[q][2*x+1]=="B":
                        ans[(m-7)*i+j]+=1  
print(min(ans))
                