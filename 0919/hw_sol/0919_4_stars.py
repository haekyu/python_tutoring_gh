def prt_stars():
	# For upper triangle
	for i in range(1, 6):
		# For the left triangle
		prt_str = (' ' * (5 - i)) + ('*' * i)

		# For the right triangle
		prt_str += ('*' * i) + (' ' * (5 - i))
		print(prt_str)

	# For the lower triangle
	for i in range(4):
		# For the left triangle
		prt_str = (' ' * (i + 1)) + ('*' * (4 - i))

		# For the right triangle
		prt_str += ('*' * (4 - i)) + (' ' * (i + 1))
		print(prt_str)
		


if __name__ == '__main__':
	prt_stars()
