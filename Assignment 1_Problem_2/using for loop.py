#1.WAP to accept a word from user and reverse it
l=str(input())
c=len(l)-1
for i in l:
    d=l[c]
    print(d,end="")
    c-=1   