def add(num1,num2):
    return num1+num2
def sub(num1,num2): 
    return num1-num2 
def  mul(num1,num2): 
    return num1*num2    
def divide(num1,num2):
    return num1/num2    
num1=int(input("enter first number: ")) 
num2=int(input("enter second number: "))  
choice=int(input("enter your choice: ")) 
if choice==1:
    print(add(num1,num2))
elif choice==2:
    print(sub(num1,num2))
elif choice==3:
    print(mul(num1,num2))  
elif choice==4:
    print(divide(num1,num2))      


