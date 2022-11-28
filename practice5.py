list1=["Phil","Oz","Seuss","Dre"]
list2=[]
for i in range(len(list1)):
    a=list1[i]
    # print(a)
    b="Dr."+a
    # print(b)
    list1[i]=b
print(list1)   