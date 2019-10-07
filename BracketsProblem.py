open_list = ["[","{","("] 
close_list = ["]","}",")"]
myStr=input()
stack = [] 
for i in myStr: 
	if i in open_list: 
		stack.append(i)
	elif i in close_list:
		pos = close_list.index(i) 
		if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
			stack.pop()
if len(stack) == 0:
	print("balanced")
else:
	print("Unbalanced") 
