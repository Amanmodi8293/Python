# a = input("Enter a number:")
# print(f"Multiplication table of {a} is:")

# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")

# except:
#   print("Invalid Input!")

# print("Some important lines of code")
# print("End of program")
try:
  num = int(input("Enter a number :"))
  a = [6,4]
  print(a[num])
except ValueError:
  print("Number entered is not an integer.")

except IndexError:
  print("Index Error")