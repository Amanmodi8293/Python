marks = [2, 4, 5, 6, "Amanmodi", True, 4, 5, 6, 7, 8, 9, 13, 45, 67]
# print(type(marks))
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative Index
# print(marks[len(marks)-3]) # Positve Index
# print(marks[6-3])
# print(marks[3])

# if "6" in marks:
#   print("Yes")

# else:
#   print("No")

# Same thing applies for the string as well!

# if "modi" in "Amanmodi":
#   print("Yes")
# else:
#   print("No")

# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[1:4])
# print(marks[1:-2])
# print(marks[1:4])
# print(marks[1:15:1])
# print(marks[1:15:2])
# print(marks[1:15:3])
# print(marks[1:15:4])

lst = [(i + 1) * 5 for i in range(10) if i % 2 == 0]
print(lst)
lst = list(range(4))
print(lst)
