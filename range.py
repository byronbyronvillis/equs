def my_range(start,end,step=1):
	while start < end:
		yield start
		start += step

def gen_fn():
	yield 1
	yield 'a'
	yield False

#gen = gen_fn()
#print(next(gen))
#for i in range(0, 10):
#	print(i)
