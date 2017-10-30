from get_max import get_max_of_lst

def get_num_max(lst):
	max_val = get_max_of_lst(lst)
	max_cnt = 0
	for e in lst:
		if e == max_val:
			max_cnt += 1

	return max_cnt


# lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
# max_val = get_max_of_lst(lst)
# num_max = get_num_max(lst)
# print('max = %d, num_max = %d' % (max_val, num_max))
