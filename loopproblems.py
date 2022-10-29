#accept a number from a user
#calculate and print the sum of all the numbers
#from 1 to input number
#using for loop



oppo = int(input("enter a number"))
sum = 0
for i in range(0,oppo+1):
    sum+=i
print(sum)