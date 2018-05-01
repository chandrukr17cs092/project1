le(n>0):
        d=n%10
        n=int(n/10)
        rev=rev*10+d
    return rev

x=int(input("enter a number:"))
r=reverse(x)
print("number:", x)
print("reverse:", r)
~                    
