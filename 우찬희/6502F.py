order=1
while True:
    num=list(map(int,input().split()))
    if (num[0]==0):
        break
    w=num[0]
    r=num[1]
    l=num[2]

    if ((2*r)**2 >= w**2+l**2):
        print('Pizza {} fits on the table.'.format(order))
    else:
        print('Pizza {} does not fit on the table.'.format(order))

    order+=1
        
        

    
