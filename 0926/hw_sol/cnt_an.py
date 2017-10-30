def cnt_an():
	s = 'Love is an open door! Love is an open door! Life can be so much more!'
	lst = s.split(' ')
	cnt = 0
	for word in lst:
		if 'an' == word:
			cnt += 1
	return cnt


if __name__ == '__main__':
	cnt = cnt_an()
	print(cnt)
