

def add(a, b):
    sum = int(a) + int(b)
    return sum


def main():
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))

  sum =  add(a, b)
  print("The sum is = ", sum)
  
 
main()