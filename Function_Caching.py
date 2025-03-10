from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(5))
print("Done for 5")
print(fx(1))
print("Done for 1")


print(fx(20))
print("Done for 20")
print(fx(10))
print("Done for 10")
print(fx(5))
print("Done for 5")
print(fx(1))
print("Done for 1")
print(fx(111))
print("Done for 111")