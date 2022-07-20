input=__import__('sys').stdin.readline

while True:
    try:
        a,b=map(int,input().split())
        sum=a

        while (a//b):
            a=a//b
            sum+=a

        print(sum)

    except EOFError:
        break
