num=int(input("Enter a number"))
x,y=0,1
z=0
while x<num:
	print(x,end=",")
	z +=1
	x,y=y,x+y
print(z)

