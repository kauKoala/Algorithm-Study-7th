n=int(input())
pat=input()
pat_a=''
pat_b=''

flag=''
for i in range(len(pat)):

    if (pat[i]=='*'):
        flag='*'
        
    else:   
        if (flag==''):
            pat_a+=pat[i]
        else:
            pat_b+=pat[i]

for i in range(n):
    s=input()
    

    if (s[:len(pat_a)]==pat_a and s[-len(pat_b):]==pat_b and len(s)>=len(pat_a+pat_b)+1):
        print('DA')

    else:
        print('NE')
