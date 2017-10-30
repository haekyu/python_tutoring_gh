def get_max_of_lst(lst):
	# Initialize max_val
	max_val = -999

	# Get the maximum value in lst
	for e in lst:
		# Get the temporal max_val
		if max_val < e:
			# max_val is no longer the maximum value
			# e should be the new maximum value
			max_val = e
	return max_val


# Test
# lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
# max_val = get_max_of_lst(lst)
# print(max_val)
