#this programme is to demonstrate nested if conditions
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("can ride the rollercoaster!")
  age = int(input("what is youe age?"))
  if age > 18:
    print("your ticket cost would be 12$")
  elif 12<=age<=18:
    print("your ticket price would be 7$")
  else:
    print("your ticket cost would be 5$")
else:
  print("oops, you cannot ride the rollercoaster!")
