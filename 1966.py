t=int(input())
for i in range(t):
        n,m=map(int,input().split())
        q=list([j]for j in range(n))
        importance=list(map(int,input().split()))
        ans=sorted(importance,reverse=True)
        for k in range(n):
                q[k].append(importance[k])
        for k in range(n):
                
                 flag=True
                 for y in range(n):
                  if q[y][1]!=ans[y]:
                     flag=False
                 if flag==True:break
                 for y in range(n):
                  if q[k][1]!=ans[k]:
                    q.append(q.pop(k))
        order=1
        for x in range(n):
                if q[x][0]==m:break
                order+=1
        print(order)