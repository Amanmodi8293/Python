marks = [23, 45, 56, 67, 78, 79, 89, 90, 99]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 7):
#         print("The marks is 90, wow !")
#     index += 1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 7):
        print("The marks is 90, wow !")