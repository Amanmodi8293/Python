
# Example of hybrid inheritance.

class Baseclass:
    pass 

class Drivedclass1(Baseclass):
    pass

class Drivedclass2(Baseclass):
    pass

class Drivedclass3(Drivedclass1, Drivedclass2):
    pass

# Example of herarchical inheritance.

class Baseclass:
    pass 

class Drivedclass1(Baseclass):
    pass

class Drivedclass2(Baseclass):
    pass

class Drivedclass3(Drivedclass1):
    pass

class Drivedclass4(Drivedclass1):
    pass

class Drivedclass5(Drivedclass2):
    pass

class Drivedclass6(Drivedclass2):
    pass