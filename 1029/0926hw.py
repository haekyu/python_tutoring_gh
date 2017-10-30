# 1. list 연습1

# list 내 최대값 구하기. 
# lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때 최대값인 6을 출력해보세요.

# 힌트1) 간단하게 max(lst) 로도 구할 수 있지만, max()를 쓰지 않고 loop로 해결해 보세요.
# 힌트2) skeleton code를 이용해도 좋습니다. ??? 을 채워 넣으면 됩니다. 

# Target list
lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]

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

max_val = get_max_of_lst(lst)
print(max_val)


# 2. list 연습2

# list 내 최대값을 갖는 원소가 몇 개인지 구해보세요.
# lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때, 최대값인 6은 2개 있습니다.
# 여기서 6의 개수인 2를 출력해 보세요.
# 이 때 다음과 같은 포맷으로 출력해 보세요: 'max = 6, num_max = 2'.

lst = [2, 3, 6, 2, -1, 0, 6, 2, 3]

def get_max_of_lst(lst):

	max_val = -999

	for e in lst:
		if max_val < e:
			max_val = e
	return max_val

def get_num_max_of_lst(lst):
	num_max = 0

	for e in lst:
		if max_val == e:
			num_max = num_max + 1
	return num_max

max_val = get_max_of_lst(lst)
num_max = get_num_max_of_lst(lst)

print('max = %d, num_max = %d' % (max_val, num_max))


# 3. list 연습3

# list 내 최대값을 갖는 원소의 index를 구해보세요.
# lst = [2, 3, 6, 2, -1, 0, 6, 2, 3] 이 주어져 있을 때, 
# 최대값인 6의 index는 2, 6 입니다. 둘 중 하나를 출력해 보세요.

print("-" * 10)
lst = [-1, 2, 3, 6, 2, 0, 6, 2, 3]

max_val = get_max_of_lst(lst)

def get_index_max_of_lst(lst):
	for idx in range(len(lst)):
		print("idx:", idx)
		if lst[idx] == max_val:
			max_index = idx
	return max_index


def get_index_max_of_lst2(lst):
	for e in lst:
		print("e:", e)
		if lst[e] == max_val:
			max_index = e
	return max_index

max_index = get_index_max_of_lst(lst)

print(max_index)

print("-" * 10)
# 4. list 연습4

# 리스트 [1, 2, 3, 4, 5] 만들기.
# 다음 <start>, <end>, 그리고 <do> 안을 채워서 위의 리스트를 만들도록 해 보세요.

# lst = list()
# for i in range(<start>, <end>):
# 	<do>
# 힌트1) 어떤 list의 맨 마지막에 어떤 원소를 덧붙이고 싶을 때 append라는
# 		함수를 사용할 수 있습니다. 
# 		예를 들어, lll이라는 리스트에 0 을 append 한다고 해 봅시다.
# 		lll = [3, 2, 1]
# 		lll.append(0)
# 		을 하게 되면 lll은 [3, 2, 1, 0] 이 됩니다.


def make_list():
	lst = list()
	for i in range(1, 6):
		lst.append(i)
	return lst

print(make_list())


# 5. list 연습5

# 리스트 [1, 2, 3, 4, 5] 만들기.
# append를 쓰지 않고 1, 2, 3, 4, 5를 만들어 보세요.
# 단, hard-coding (내가 손으로 일일이 1, 2, 3, 4, 5 타이핑하기) 는 안됨.

def make_list2():
	lst = [i for i in range(1, 6)]
	return lst

print(make_list2())

# list comp 연습
# 1 부터 10 까지 자연수 중에서, 짝수인 것을 모은 리스트를 만들어 봅시다
[2, 4, 6, 8, 10]
lst = []
for i in range(1, 11):
	if i % 2 == 0:
		lst.append(i)

[i for i in range(1, 11) if i % 2 == 0]

# 6. string 연습1

# 스트링으로 된 문장 내부에 특정 word가 몇 번 포함되는지 찾기.
# 예를 들어, str과 같은 문장이 주어져 있고, 'an' 이라는 단어가 str 내부에 몇 번 나타나는지 찾기.
# str = 'Love is an open door! Love is an open door! Life can be so much more!'
# 일 때, an 이 두 번 있으니 2를 프린트하게 해 보세요.

# 힌트1) str을 ' ' (띄어쓰기) 기준으로 잘라 list에 보관할 수 있습니다.
# 		예) lst = str.split(' ') 을 하게 되면
# 			lst 는 ['Love', 'is', 'an', ...] 이 됩니다.

str = 'Love is an open door! Love is an open door! Life can be so much more!'

lst = str.split(' ')

def num_str():
	num_str = 0
	for e in lst:
		if e == 'an':
			num_str = num_str + 1
	return num_str

print(num_str())


# 7. string 연습2

# 스트링으로 된 문장 내부에 특정 문구가 몇 번 포함되는지 찾기.
# 예를 들어, str과 같은 문장이 주어져 있고, 'an' 이 str 내부에 몇 번 나타나는지 찾기.
# str = 'Love is an open door! Love is an open door! Life can be so much more!'
# 일 때, an 이 세 번 검색되고 있으니 3을 프린트하게 해 보세요.
# 세 번의 an 은 아래와 같이 검색됩니다. (*** 안에 있음.)
# Love is ***an*** open door!
# Love is ***an*** open door!
# Life c***an*** be so much more!

# 힌트1) string의 membership 기능을 이용하면 편리합니다.
# 		어떤 string 안에 특정 string이 포함되는지 알 수 있습니다.
# 		예를 들어, 'abc' 가 'xxabcxxxxxxx' 에 포함되는지 알고 싶으면
# 		'abc' in 'xxabcxxxxxxx' 를 실행시켜 보세요. True 가 나옵니다.

# Short Ver.
str = 'Love is an open door! Love is an open door! Life can be so much more!'
print(str.count('an'))

# Long Ver.
str = 'Love is an open door! Love is an open door! Life can be so much more!'
lst = str.split(' ')

def num_str2():
	num_str2 = 0
	for e in lst:
		if 'an' in e:
			num_str2 = num_str2 + 1
	return num_str2

print(num_str2())




