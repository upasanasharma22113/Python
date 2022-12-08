from datetime import date


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

d = date(year, month, day)
print(d)


#List are used store multiple non-homogeneous data in a single variable
# ordered
# Changable
# Allows duplicate value
# 
# Insert() - insert item  at specified index
# Append() - insert item at the end of the list
# Extend() - it appends elements from one list to another list, it can be used to append different collection
# Remove() - removes item from a specified index
# pop()
# clear() - clears all elements
# range(), len()
# sort() - it will sort the list in ascending order
# copy() 