x=list(input())
for i in range(len(x)):
    if 64<ord(x[i])<91:
        x[i]=chr(ord(x[i])+32)
        
d={}

#d={m:0,i:0,s:0,p:0}

for i in (set(x)):
    d[i]=0
    for j in range(len(x)):
        if x[j]==i:
            d[i]+=1

if len(set(x))==1:
    d["temp"]=0
    
sorted_d=sorted(d.items(), key=lambda item:item[1], reverse=True)

if sorted_d[0][1]==sorted_d[1][1]:
    print("?")
else:
    print(chr(ord(sorted_d[0][0])-32))
