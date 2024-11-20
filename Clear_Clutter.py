import os 

files = os.listdir("ClutterFolder")
 
i = 1
for file in files:
    if file.endswith(".png"):
     print(file)
     os.rename(f"ClutterFolder/{file}", f"ClutterFolder/{i}.png")
     i = i + 1