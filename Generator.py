def my_generator():
    for i in range(50):
        yield i 

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen: 
    print(i)