num=input("enter a number")
if num.isdigit():
	a=num[::-1]
	if num==a:
		print("Palindrome Number")
	else:
		print("not Palindrome number")
else:
	print("Not a number")