def inputt():
    n = int(input("Enter a number: "))  
    return n
def add(a,b):
    sum = a + b
    return sum

def outputt(a,b,sum):
    print("Sum of", a, "and", b, "is", sum)

def mains():
    a=inputt()
    b=inputt()
    sum=add(a,b)
    outputt(a,b,sum)
mains()