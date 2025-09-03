a = int(input("enter a number"))
b = int(input("enter a number"))

# with params and with return type
def addition(d,e):
    return d + e

print("A + B", a +b)
print("A + B using a function",addition(a,b))


# 

def add2():
    f = 12
    h = 13
    return f + h

print("fucntion with out prams and with return",add2())


def add3(s,t):
    print("with params with out return", s + t)
    
add3(a,b)


def add4():
    z = 12
    y = 34
    print("without param sand return", z+y)

add4()