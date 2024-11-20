class Vector:
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z"
    
    def __add__(self, i):
        return Vector(self.x + i.x, + self.y + i.y, + self.z + i.z)

v1 = Vector(1,2,3)
print(v1)
v2 = Vector(3,2,1)
print(v2)
print(v1 + v2)
print(type(v1 + v2))