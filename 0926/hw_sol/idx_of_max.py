from get_max import get_max_of_lst

def get_idx_of_max(lst):
	max_val = get_max_of_lst(lst)
	for idx, e in enumerate(lst):
		if e == max_val:
			return idx

lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]
print(get_idx_of_max(lst))
