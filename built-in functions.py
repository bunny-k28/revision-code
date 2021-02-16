# append function
list1.append()  # <variable>.<function>, adds at the end
print(list1)

# count function
print(list1.count(1))

# remove function
list1.remove('hello')  # accepts direct value

# index function
y = list1.index('hello')
print(y)

# pop function
list1.pop(2)  # accepts index value
print(list1)

# extend function
list2 = [6, 8, 9, 7]
list1.extend(list2)  # add another list in list
print(list1)

# sort function
list1.sort()  # True - yes and false - no
print(list2)

# int - integer
# str - string
# eval - integer + string both

# while loop
x = 1  # counter or incrementing value
while x<=5:
     print('hello')
     # break  # statement to end the any loop
     x = x + 2  # incrementation value
print('loop ended')

# for loop
# case 1
for i in list2:
     print(i, end='')  # end key word to print horizontaly

# for loop case 2
for i in range( 0, 5):
     print(i)
