t = int(input())
for _ in range(t):
	grid = [[]]
	for i in range(3):
		each_row = [str(x) for x in input()]
		grid.append(each_row)

	#print(grid)

	count_X , count_O , count__ = 0 , 0 , 0

	for i in range(1 , 4):
		for j in range(3):
			if grid[i][j] == 'X':
				count_X += 1
			elif grid[i][j] == 'O':
				count_O += 1
			else:
				count__ += 1


	win_X = False
	win_O = False

	if grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] =='X':
		win_X = True
	if grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] =='X':
		win_X = True
	if grid[3][0] == 'X' and grid[3][1] == 'X' and grid[3][2] =='X':
		win_X = True

	if grid[1][0] == 'X' and grid[2][0] == 'X' and grid[3][0] =='X':
		win_X = True
	if grid[1][1] == 'X' and grid[2][1] == 'X' and grid[3][1] =='X':
		win_X = True
	if grid[1][2] == 'X' and grid[2][2] == 'X' and grid[3][2] =='X':
		win_X = True

	if grid[1][0] == 'X' and grid[2][1] == 'X' and grid[3][2] =='X':
		win_X = True
	if grid[1][2] == 'X' and grid[2][1] == 'X' and grid[3][0] =='X':
		win_X = True



	if grid[1][0] == 'O' and grid[1][1] == 'O' and grid[1][2] =='O':
		win_O = True
	if grid[2][0] == 'O' and grid[2][1] == 'O' and grid[2][2] =='O':
		win_O = True
	if grid[3][0] == 'O' and grid[3][1] == 'O' and grid[3][2] =='O':
		win_O = True

	if grid[1][0] == 'O' and grid[2][0] == 'O' and grid[3][0] =='O':
		win_O = True
	if grid[1][1] == 'O' and grid[2][1] == 'O' and grid[3][1] =='O':
		win_O = True
	if grid[1][2] == 'O' and grid[2][2] == 'O' and grid[3][2] =='O':
		win_O = True

	if grid[1][0] == 'O' and grid[2][1] == 'O' and grid[3][2] =='O':
		win_O = True
	if grid[1][2] == 'O' and grid[2][1] == 'O' and grid[3][0] =='O':
		win_O = True


	"""
	if count__ != 0:
		if count_X == 5 and count_O == 4:
			print("1")
		else:
			print("3")

	else:
		if count__ % 2 == 0:
			if count_X != count_O + 1:
				print("3")
		if count__ % 2 != 0:
			if count_X != count_O:
				print("3")
			else:
				print("2")

		if win_X == True:
			if count_X != count_O + 1:
				print("3")

			else:
				print("1")

		else:
			if count_X != count_O:
				print("3")

			else:
				print("1")

		if win_X == True and win_O == True:
			print("3")

		"""
	if (win_X == True and win_O == True) or (count_X < count_O) or (count_X > count_O + 1):
		print("3")

	elif count_X == 0 and count_O == 0 and count__ == 9:
		print("2")

	elif win_X == True and win_O == False and count_X == count_O + 1:
		print("1")
	elif win_X == False and win_O == True and count_X == count_O:
		print("1")
	elif count__ % 2 != 0:
		if count_X == count_O:
			print("2")
		else:
			print("3")
	elif count__ % 2 == 0 and count__ != 0:
		if count_X == count_O + 1:
			print("2")
		else:
			print("3")
	elif win_X == False and win_O == False:
		if count__ != 0:
			print("2")
		else:
			if count_X == count_O + 1:
				print("1")
			else:
				print("3")

	else:
		print("3")



