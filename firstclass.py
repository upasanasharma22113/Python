# store multiple values in single variable

# unordered
myset = {"car", "bike", "boat"}
print(myset)

# unchangable
# duplicates are not allow
myset = {"car", "bike", "boat","car"}
print(myset)
# for a in myset:
#     if a =="bike":
#         print("True")
#     else:
#         print("False")   

if "boat" in myset:
        print("True")  
else:
        print("False")    


sets= {1,2,3,4,5,6,7}
print(len(sets))
sets.add(10)    
print(sets)           #those thing are unchangable we use add to add something in it
