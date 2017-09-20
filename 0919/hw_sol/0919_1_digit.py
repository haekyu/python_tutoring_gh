# Sol 0
def digit_0(x):
	# x = |x|
	if x < 0:
		x = -x

	# Get digit of x
	digit = 0
	while True:
		digit += 1
		x = int(x / 10)
		if x <= 0:
			break

	return digit

# Sol 1
def digit_1(x):
	# x = |x|
	if x < 0:
		x = -x

	# Get digit of x
	digit = len(str(x))

	return digit


if __name__ == '__main__':
	for test in [-923, 0, 1, 3, 23, 4324]:
		print('-' * 10)
		d = digit_1(test)
		print(d)
