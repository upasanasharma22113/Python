mytuple=("car", "bus", "truck")
for x in  mytuple:
    print(x)

# while loop  
i=0  
while i<len(mytuple):
    print(mytuple[i])
    i+=1

# LIST INSIDE TUPLE
tuple1= (1,[6,7],2,3,4,5)
a= tuple1[1][0]
print(a)

# REPLACE 6 WITH 8
tuple1= (1,[6,7],2,3,4,5)
a= tuple1[1][0]
tuple1[1][0]=8
print(tuple1)





