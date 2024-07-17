# Write your code below this line 👇
def prime_checker(number):
  #numbers = range(1,number)
  index = 1
  total = 0
  while index <= number:
    if number % index == 0:
        total += 1
    index += 1
  if total == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
