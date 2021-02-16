# LHS are variables

string = "123"  # immutable, more char can be added
integer = 123  # immutable
floot = 1.54  # decimal values, immutable
lists = []  # empty list, mutable or can be changed(addition or subtraction)
tuples = ()  # empty tuple, immutable or can't be changed
dicts = {key: value}  # dictionary accepts values/elements in key: value pair. for ex:- {1: '123'}
sets = {1, 'str', 1}  # => sets do not store any element more than once. for ex:- {1, 'str'}

# slicing of string
str1 = 'arman'
print(str1[4:0:-2])  # (-) with step value for reverse slicing, <variable>[start:end:step], default step value is 1
# output--> nm

# list slicing
list1 = [1, 2, 'hello', 1.3, 1]
print(list1[0:3])  # (-) with step value for reverse slicing, <variable>[start:end:step], default step value is 1
# output--> [1, 2, 'hello']

# formula for slicing
# <variable>[l:m:n]   where l-start value, m-end value, n-index
# output--> [index value of l till index value of m -1] this formula is for without step value

# input statements key words:-
# int - takes integer as input
# str - takes string as input
# eval - takes both string as well as integer as input
