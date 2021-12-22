def greatest(n1,n2,n3):
    if n1 > n2 and n1 >n3:
     g=n1
    elif n2 > n1 and n2 > n3:
     g = n2 
    else:
     g = n3
    return g

a = greatest(2,4,3)
print(a)
    