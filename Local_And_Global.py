a = 4
print("The global a is : " , a)

def Aman():
    global a
    a = 5
    # print("The local a is : ", a)
    # print("Hello, Aman. " , a)

print("The global a is : " , a)
Aman()
print("The global a is : " , a)
a = 6
print("The global a is : " , a)