def input_n():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    return a,b
  
def add(a, b):
    sum = float(a)+float(b) 
    return sum
  
def output(a, b, sum):
    print("The sum of ",a ,"and", b ,"is",sum)  
  
def main():
    a, b = input_n()
    res = add(a, b)
    output(a, b, res)

if __name__ == '__main__':
    main()