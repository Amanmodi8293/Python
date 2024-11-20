
# READING A FILE

# f = open("myfile.txt", "r")
## print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open("myfile.txt", "w")
# f.write("Hello, World!")
# f.close()

# Appending A FILE

f = open("myfile.txt", "a")
f.write("Hello, World!")
f.close()

with open("myfile.txt", "a") as f:
    f.write("I am inside with.")