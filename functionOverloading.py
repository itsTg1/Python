def add1(a,b):
    return a+b

def add2(a,b):
    strin=a+b
    return strin

def add3(a,b):
    a=a+b
    return a

def add(a,b):
    if(type(a)==int and type(b)==int):
        return add1(a,b)
    elif(type(a)==str and type(b)==str):
        return add2(a,b)
    elif(type(a)==list and type(b)==list):
        return add3(a,b)

print(add(2,3))
print(add("rahul","roy"))
print(add([2,3,21],[334,214]))

# method-2

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
