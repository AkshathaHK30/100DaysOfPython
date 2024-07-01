print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# trying to convert the names to lower cases words in below 2 lines
first_name = name1.lower()
second_name = name2.lower()
count = 0
love = 0

#trying to get the TRUE word's letter count in the below piece of code from the first name using the native method
for i in first_name:
  if i == 't':
    count += 1
  if i == 'r':
    count +=1
  if i == 'u':
    count += 1
  if i == 'e':
    count += 1
  else:
   count += 0
#print(count)

#trying to get the TRUE word's letter count in the below piece of code from the second name using the count function
count += second_name.count('t')
count += second_name.count('r')
count += second_name.count('u')
count += second_name.count('e')
#print(count)

#trying to get the LOVE word's letter count in the below piece of code from the first name using the native method
for i in first_name:
  if i == 'l':
    love += 1
  if i == 'o':
    love +=1
  if i == 'v':
    love += 1
  if i == 'e':
    love += 1
  else:
   love += 0

#trying to get the LOVE word's letter count in the below piece of code from the second name using the count function
love += second_name.count('l')
love += second_name.count('o')
love += second_name.count('v')
love += second_name.count('e')
#print(love)

#concatinating the true word's count and Love word's count to get the total love score
total = str(count)+str(love)
#print(total)

if int(total)< 10 or int(total)>90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 40<=int(total)<=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
