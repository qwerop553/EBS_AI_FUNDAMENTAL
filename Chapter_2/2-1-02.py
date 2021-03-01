a = [242, 256, 237, 223, 263, 81, 46]
print('A =', a)

n = len(a)
my_sum = 0
i = 0

for b in a:
	my_sum += b

my_avg = my_sum/n
print("Total Sum:", my_sum)
print("Total Average:",my_avg)
