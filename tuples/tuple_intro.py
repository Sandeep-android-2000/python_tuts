
'''
intro to tuple :
1. A tuple is a collection which is ordered and unchangeable.
2. Tuples are written with round brackets.
3. Tuple items are indexed, the first item has index [0], 
   the second item has index [1] etc.

4. Range of Indexes:

   4.1. You can specify a range of indexes by specifying 
   where to start and where to end the range.

   4.2. When specifying a range, the return value will be 
   a new tuple with the specified items.



5. Change Tuple Values:

   5.1. Once a tuple is created, you cannot change its values. 
        Tuples are unchangeable, or immutable as it also is called.

   5.2. But there is a workaround. You can convert the tuple into a 
        list, change the list, and convert the list back into a tuple.

6. You are allowed to add tuples to tuples, so if you want to 
   add one item, (or many), 
   create a new tuple with the item(s), and add it to the existing tuple:

7. in Python, we are also allowed to extract the values back into variables. 
   This is called "unpacking":


8. Using Asterisk*
   If the number of variables is less than the number of values, 
   you can add an * to the variable name and the values will be 
   assigned to the variable as a list:
'''





my_tuple = ("apple", "banana", "cherry")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

'''



'''

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)