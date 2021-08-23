t = int(input())
for i in range(t):
	n, m = map(int, input().split())
	num_div = 0
	count1 = 0
	count2 = 0
	arr_nondiv = []
	for i in range(2, int(n**(1/2))):
		if m%i == 0:
			count1 += 1
		else:
			arr_nondiv.append(i)

	count2 = n - (count1 + 1)
	curr_rem = 0
	global_rem = 0
	count_same_rem = 1
	for j in arr_nondiv:
		curr_rem = m % j
		if global_rem != curr_rem:
			global_rem = curr_rem
		else:
			count_same_rem += 1

	print(n-1 + (count1*(count1 - 1))//2 + (count_same_rem*(count_same_rem - 1))//2 ) # sum of 1's pairs + div pairs + non_div same remainder pairs


