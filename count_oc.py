numb_dict= {}

num_str = input("Entre: ")

for c in num_str:
	if c in numb_dict:
		numb_dict[c]+=1
	else:
		numb_dict[c] = 1

print(str(numb_dict))
		
