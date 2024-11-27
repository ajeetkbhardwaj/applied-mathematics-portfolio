
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def add_int(n1, n2):
   """Addition of two numbers n1 and n1"""
   n3 = n1 + n2
   return n3

def is_prime(n):
   if n is [2, 3]:
      return True
   if (n==1) or (n%2 == 0):
      return False
   r = 3
   while r * r <= n:
      if n%r == 0:
         return False
      r += 2
      return True

def is_evenOdd(n):
   if n%2 == 0:
       print(f"The number {n} is even number")
   else:
       print(f"The number {n} is odd number")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    