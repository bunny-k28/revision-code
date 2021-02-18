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
     
     
# Fibonacci sequence
terms = 10
# first two terms
num1, num2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < terms:
    print(num1, end="  ")
    temp = num1 + num2
    # update values
    num1 = num2
    num2 = temp
    count += 1
     
     
# printing this pattern:-

 '''1
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5'''
     
n = int(input('no. of rows: ')) # no. of rows as per the user choice
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))


# take n no. of integers from user using loop and print their average value on the screen.
xyz = int(input('enter no. inputs: '))  # no of times the loop will execute, user choice
abc = 1  # counter value/incrementing value
lib = []  # list
while abc <= xyz:  # <counter value> <logic> <times of loop>
    num = int(input('enter no.'))  # sup. 1
    lib.append(num)
    abc += 1  # xyz = xyz + 1
avg = sum(lib)/2
print(avg)


# take 10 integers from user using loop and print their average value on the screen.
xyz = 10  # no of times the loop will execute, as per the Q.
abc = 1  # counter value/incrementing value
lib = []  # list
while abc <= xyz:  # <counter value> <logic> <times of loop>
    num = int(input('enter no.'))  # sup. 1
    lib.append(num)
    abc += 1  # xyz = xyz + 1
avg = sum(lib)/2
print(avg)
