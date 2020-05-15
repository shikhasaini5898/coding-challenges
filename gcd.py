#gcd...

a=int(input("enter the number"))
b=int(input("enter the number"))
def Gcd(a,b):
    if a==0:
        return b
    else:
        return Gcd(b%a, a)
if Gcd(a,b):
    print(Gcd(b%a,a))
else:
    print("False")
    
