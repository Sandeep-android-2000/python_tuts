#append --> used to insert at end position

fruits = []
fruits.append("mango")
fruits.append("guava")
fruits.append("apple")
#print(fruits)

#insert method --> used to insert at any position

fruits.insert(1,"oranges")
#print(fruits)

#concatenate --> join two lists
fruits1 = ['oranges','guava']
fruits2 = ['apple','grapes']

fruits = fruits1 + fruits2

# print(fruits)

#extend method --> To append elements from another list to the current list


#   append vs expand :

'''
1. In append() we add a single element to the end of a list. 

2. In extend() we add multiple elements to a list. 

3. The supplied element is added as a single item at the end 
   of the initial list by the append() method. 

4.  When an Iterable is supplied as a parameter, the extend() 
    method adds each element from the Iterable to the list’s end 
    individually. It alters the initial list.    
'''                         
       
fruits1.extend(fruits2)
# print(fruits1)

# difference b/w append and extend
# my_list = ['geeks', 'for']
# another_list = [6, 0, 4, 1]
# my_list.append(another_list)
# print(my_list)


my_list = ['geeks', 'for']
another_list = [6, 0, 4, 1]
my_list.extend(another_list)
# print(my_list)

#delete from lists

# 1. pop

# 1.1 no argumnent passed

# print(my_list.pop())
# print(my_list)

# 1.2 specified item
# print(my_list.remove(6))
# print(my_list)

# 1.3 specified index

# print(my_list.pop(3))
# print(my_list)

# 2.  The del keyword also removes the specified index:
# print(my_list)
# del my_list[3]
# print(my_list)

# 2.1The del keyword can also delete the list completely.
# del my_list
# print(my_list)


