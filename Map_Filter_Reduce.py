# # def cube(x):
# #     return x*x*x

# # print(cube(5))

# l = [2,4,3,4,5,6,7,4,8]

# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# def filter_function(a):
#     return a==4

# newnewl = list(filter(filter_function, l))
# print(newnewl)

from functools import reduce
# list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
# Calculate the sum of numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Print the sum
print(sum)