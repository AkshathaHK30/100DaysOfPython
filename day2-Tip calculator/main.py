#This is a repository to create tip calculator which we can use to split the bill among certain number of people with added tip to the bill
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
# we can convert the above output of tip to certain datatype by wrapping up the input function
#for ex: tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = input("How many people to split the bill? ")
percentage = float(total_bill) + (float(total_bill) * (float(tip)/100))
ind_pay = float(percentage) / float(split)
final = round(ind_pay,2)
#we can use format function to round specific decimal number to 2 digits
final = "{:.2f}".format(ind_pay)
print(f"Each person should pay: ${final}")
