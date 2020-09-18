import math
a=int(input("Enter side:"))
b=a
c=a
h=math.sqrt(a**2-b/2**2)
print(h)
l=a*h/2
print(l)
r=int(input("Enter radius:"))
П=3.14
s=П*r**2
print(s)
space=l-s
print(space)