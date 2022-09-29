
def my_sum(l):
	i=0
	n=10
	total = 0
	while i < len(l):
		total += l[i]
		i += 1

	return total

l = [5,10,15,50]
g = [67,67,34,34]

print(my_sum(l))
print(my_sum(g))
