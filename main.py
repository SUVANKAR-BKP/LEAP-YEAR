# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# calculating is clearly divisible by 4 or not

check_divisible_by_four = year % 4
check_divisible_by_hundred = year % 100
check_divisible_by_400 = year % 400

if check_divisible_by_four == 0 :
	if check_divisible_by_hundred == 0 :
		if check_divisible_by_400 == 0 :
			print("This is leap year")
		else:
			print("This is not leap year")
	else:
		print("This is leap year")
else:
	print("This is not leap year")
