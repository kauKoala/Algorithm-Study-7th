x,y,w,h=map(int,input().split())



list=[]
list.append(x)
list.append(y)
list.append(h-y)
list.append(w-x)

print(min(list))



