def prt_times_table():
	for i in range(1, 10):
		for j in range(1, 10):
			print('%d * %d = %d' % (i, j, i * j))


if __name__ == '__main__':
	prt_times_table()
