a,b,c,d=(map(int,input().split()))





for i in range(4):
    a,b,c,d=(map(int,input().split()))
    cnt=0

    list=[]
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)

    if 1 ==list[i]:
        cnt+=1
if cnt==0:
    print("D")
    
if cnt==1:
    print("C")
   
if cnt==2:
    print("B")
   
if cnt==3:
    print("A")
   
if cnt==4:
    print("E")
 
        

