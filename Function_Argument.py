# def averagenumber(a=5=4,b=6):
# def averagenumber(a,b,c=6):
#   average = (a+b+c)/2
#   print("The average is : ",average)

# averagenumber()
# averagenumber(4,6)
# averagenumber(4)
# averagenumber(b=10)
# averagenumber(b=10,a=20)
# averagenumber(4,6) # The value is Required.

# def name(fname,mname = "Jhon",lname = "Whatson"):
#   print("Hello", fname, mname, lname)

# name("Aman", "Modi", "Chourasiya")


def averagethevalue(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("The average is : ", sum / len(numbers))
  # return 400
  return sum / len(numbers)


c = averagethevalue(2, 6, 4, 8)
print(c)

# def name(**name):
#   print(type(name))
#   print("Hello", name["fname"], name["mname"], name["lname"])

# name(fname = "Aman", mname = "Modi", lname = "Chourasiya")
