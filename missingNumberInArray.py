n=int(input())
a=list(map(int,input().split()))
sum1=(n*(n+1)//2)
sum2=0
for i in a:
    sum2=sum2+i
print(sum1-sum2)    