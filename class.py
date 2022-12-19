# # pass is for empty class
# class Laptop:
#     def __init__(self):
#         print("hello world")


#     def config(self):
#         print("Asus","17","1TB")
# laptop1=Laptop()
# laptop2=Laptop()
# Laptop.config(laptop1)
# Laptop.config(laptop2)

# laptop1.config()
# laptop2.config()



class student:
 def __init__(self,name,rollNo):
    self.name=name
    self.rollno=rollNo
 def info(self):
    print("name is :",self.name,"roll number is : ",self.rollno)
student1= student("shivani","65")
student2= student("upasana","47")
student1.info()
student2.info()

print(id(student2))
print(id(student1))




class person:
    def __init__(self):
        self.name="ishan"
        self.number=32
    def compare(self, other):  
        if(self.number==other.number):
            return True 
        else:
            return False

p1=person()
p2=person()   

if p1.compare(p2):
    print("same")
p2.number=18
print(p1.number)
print(p2.number)
# print(p1.name)   
# print(p2.number)
# p1.name="upasana"
# p2.name="shivani"
# print(p1.name)
# print(p2.name)
