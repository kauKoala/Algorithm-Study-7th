s=''
while True:
    try:
        line=input()
        s+=line
    except EOFError:
        break
arr=list(map(int,s.split(',')))
print(sum(arr))
