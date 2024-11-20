# dic = {
#     45: "Harry",
#     55: "Spoon",
# }
# print(dic[45])
# print(dic[55])
info = {'name': 'Karan', 'age': 19, 'eligible': True}
# print(info)
# print(info.keys())
# print(info.values())
# print(info['name'])
# # print(info['name2']) # throws error
# print(info.get('name'))
# print(info.get('name2'))  # Does not throws error
# print(info['age'])
# print(info['eligible'])

# for key in info:
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")
