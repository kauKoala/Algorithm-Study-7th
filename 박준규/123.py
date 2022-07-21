a, b, c = map(int, input().split())
a1 = a*b/c
a2 = a/b*c
if a1>=a2:
    print(int(a1))
else:
    print(int(a2))