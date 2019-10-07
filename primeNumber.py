num=int(input("Enter a number"))
for i in range(2,num):		#there is no need to treverse at num here you can also traverse only num//2
	if num%i==0:
		print("Not a Prime Number")
		break
	else:
		print("Prime number")
		break