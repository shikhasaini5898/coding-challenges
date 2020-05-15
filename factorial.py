#factorial program...


n=int(input("enter the number"))
def Factorial(n):
    while n==1:
        return n
    if n<1:
        return NA
    else:
        return(n*Factorial(n-1))
print(Factorial(int(n)))        
        
        