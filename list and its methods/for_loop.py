# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x,end = " ")

#list constructor

'''
numbers = list(range(1,11))
# print(numbers)

numbers.extend([1,7,9,6,4,8])
print(numbers)
print(numbers.index(1,3,14))
'''

'''
def square(nums):

    sq_nums=[]
    for x in nums:
        sq_nums.append(x*x)
    return sq_nums

nums = []

for i in range(1,5):
    nums.append(i)

square_nums = square(nums)
print(square_nums)

'''

'''
def reverse(strings):
    new_strings = []
    for string in strings:
        new_strings.append(string[::-1])
    return new_strings


strings = ['abc','pqr','xyz']
strings = reverse(strings)

print(strings)
'''

'''
def find_common(nums1,nums2):
    list = []
    for ele in nums1:
        if ele in nums2:
            list.append(ele)
    return list

nums1 = [1,2,5,8]
nums2 = [1,2,7,6]


common_list = find_common(nums1,nums2)
print(common_list)
'''

def func(matrix):

    cnt = 0
    for ele in matrix:
        if type(ele) == list:
            cnt += 1
    return cnt  
matrix = [1,2,3,[1,2],[3,4,5]]


print(func(matrix))

# print(no_of_list)



