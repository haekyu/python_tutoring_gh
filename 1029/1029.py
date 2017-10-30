import time

# lst = []
# 100000개의 30을 append 하면 느리고

# lst = [0] * 100000
# for idx in range(100000):
# 	lst[idx] = 30

id_lst = ['asdfsdfsdf', 'rewef', 'aaa', 'bbb']

map_dict = {}
n = 0
for uid in id_lst:
	map_dict[uid] = n
	n += 1

num_user = n

# lst1 = [1, 2, 3, 0]
# lst2 = ['a', 'b', 'c', 'd']
# for e1, e2 in zip(lst1, lst2):
# 	print(e1, e2)


fruit_color_dict = dict()

fruit_color_dict["apple"] = "red"
fruit_color_dict["tomato"] = "red"
fruit_color_dict["orange"] = "orange"
fruit_color_dict["fig"] = "pink"

name_lst = ["apple", "orange", "fig"]
color_lst = ["red", "orange", "pink"]

print("=" * 10)
def search(fruit_name, name_lst, color_lst):
	for fruit, color in zip(name_lst, color_lst):
		if fruit == fruit_name:
			fruit_color = color

	# for idx in range(len(name_lst)):
	# 	if name_lst[idx] == fruit_name:
	# 		fruit_color = color_lst[idx] 

	# for fruit in name_lst:
	# 	if fruit == fruit_name:
	# 		x = name_lst.index(fruit)
	# 		fruit_color = color_lst[x]

	return fruit_color

start = time.time()
fig_color = fruit_color_dict["fig"]
print(fig_color)
end = time.time()
print('Dictionary: %s sec' % (end - start))

start = time.time()
fig_color = search("fig", name_lst, color_lst)
print(fig_color)
end = time.time()
print('List: %s sec' % (end - start))


# Stack
# stack = list()

# def push(val, stack):
# 	stack.append(val)


# def pop(stack):
# 	del stack[idx]
# 	last = 가장 마지막에 들어온 값
# 	그 last는 stack에서 지워져야 함
# 	return last 




# Call by value
# copy를 인풋으로 주기

a = 3
def add_value(x):
	x = x + 10

add_value(a)
print(a)


# Call by reference
lst = []
def add_val(l):
	l.append(0)

add_val(lst)
print(lst)
