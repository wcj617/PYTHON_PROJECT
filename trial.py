def plus(a,b):
    return int(a) + int(b)

def minus(a,b):
    return int(a) - int(b)

def multiply(a,b):
    return int(a) * int(b)

def divide(a,b):
    return int(a) / int(b) if int(b) else "invalid number"

def negate(a):
    return -int(a)

def power(a,b):
    return int(a) ** int(b)

def remainder(a,b):
    return int(a) % int(b)

print(plus(3,"7"))
print(minus("9",1))
print(multiply("10",2))
print(divide("9","3"))
print(divide("9","0"))
print(negate("-3"))
print(power("10",2))
print(remainder("9","3"))