n = int(input("enter a number here :"))

def sumN(n):
  sum  = 0

  while n > 0 :
    digit = n%10
    sum = sum + digit
    n = n//10
  return sum 

print("sum :",sumN(n))
