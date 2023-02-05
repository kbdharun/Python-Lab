# Q6. To display the factors, prime factors of a given number

import math

# Finding factors

def factors(n):
  for i in range(1, n+1):
    if(n%i==0):
      print(i,end=" ")

# Check if a number is prime or not

def isPrime(n):
  if(n==0 or n==1):
    return False
  prime = True
  for i in range(2,n-1):
    if(n%i == 0):
      prime = False
      break
  return prime

# Finding prime factors

def primeFactors(n):
  for i in range(2, n-1):
    if(n%i==0 and isPrime(i)):
      print(i, end=" ")

n = int(input("Enter the value of n: "))
print(f"\nThe factors of {n} are:")
factors(n)
print(f"\n\nThe prime factors of {n} are: ")
primeFactors(n)