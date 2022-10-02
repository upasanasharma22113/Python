import math
b= float(input("enter first side--"))
a= float(input("enter second side--"))
c= float(input("enter third side--"))
s= a/2+b/2+c/2
z=s-a
y=s-b
x=s-c
print(math.sqrt(s*x*y*z))

