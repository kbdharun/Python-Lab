# Q3. Program to Print Prime Factors

'''
Write function to print prime factors of the given number to implement enclosing function scope.
    • Consider an outer function called ‘Factors()’ to find the factors of an integer (N) from the
user.
    • Include ‘isprime()’ as the inner function within the outer function to check whether the factor in
outer function is prime or not. And print the prime factor
'''

import math
def Factors(n):
  def isPrime(n):
    if n==0 or n==1:
      return False
    success = True
    for i in range(2,int(math.sqrt(n))+1):
      if n%i == 0:
        success = False  # n is not prime
        break
    return success
    
  for i in range(1,n+1):
    if n%i==0 and isPrime(i):
      print(i, end=" ")

print('''
Prime Factors Calculator
=======================
''')
num = int(input("Enter a number: "))
print("The Factors of the given number are:")
Factors(num)