a=list(map(int,input().split()))
def leaders(a):
    b=a[::-1]
    print(b)
    c=len(b)
    print(c)
    if c==1:
        return a
    out=[]
    out.append(b[0])
    max=b[0]
    for i in range(1,c):
        if b[i]>=max:
            out.append(b[i])
            max=rev[i]
        return out
out=leaders(a)
print(out)