# void 함수
def f(x, y=0, z=1):
	print(x, y, z)

def h(lst):
	lst[0] = 0

def p(x):
	x = 0
	

# non-void 함수
def g(x):
	return x + 1


result = g(3)
print('result: %s' % result)

result2 = f(1, 1, 1)
print('result: %s' % result2)


import numpy

'''
M = 2 3
    4 5
    6 7
m_lst = [[2, 3], [4, 5], [6, 7]]
m_arr = numpy.array([[2, 3], [4, 5], [6, 7]])
'''



lst = [2, 3, 4, 5, 6, 7]
arr = numpy.array(lst)
# print(lst)
# print(arr)
arr2 = arr * 3
print(arr2)
# lst2 = lst + lst
# print(lst2)

import time

# sparse 행렬
row = [0, 0, 1, 1, 2, 2]
col = [0, 1, 0, 1, 0, 1]
val = [2, 3, 4, 5, 6, 7]
start = time.time()
for rcv in zip(row, col, val):
	# rcv = (r, c, v)
	r = rcv[0]
	c = rcv[1]
	v = rcv[2]
	# 수정 시도
	# rcv[0] = 300
	# rcv.append(333)
	# print(r, c, v)
end = time.time()
print('ver4: %s' % (end - start))

'''
# 만약 내가 enumerate 도 모르고 zip도 모른다면?
start = time.time()
for th in range(len(row)):
	r = row[th]
	c = col[th]
	v = val[th]
	print(r, c, v)
end = time.time()
print('ver1: %s' % (end - start))

# 만약 내가 enumerate 도 모르고 zip도 모른다면?
start = time.time()
th = 0
for r in row:
	c = col[th]
	v = val[th]
	print(r, c, v)
	th = th + 1
end = time.time()
print('ver2: %s' % (end - start))

# 만약 내가 zip을 모른다면?
start = time.time()
for th, r in enumerate(row):
	c = col[th]
	v = val[th]
	print(r, c, v)
end = time.time()
print('ver3: %s' % (end - start))
'''
'''
# zip
lst1 = [3, 2, 1, 6, 3, 2, -1, 3, 5, 2]
lst2 = [1, 2, 0, 6, 3, 2, -1, 3, 5, 3]
for e1, e2 in zip(lst1, lst2):
	print(e1, e2)          
  
# 중도 중단 (break)
lst = [3, 2, 1, 6, 3, 2, -1, 3, 5, 2]
for eth, e in enumerate(lst):
	if e < 0:
		print('break???')
		break
	print('%d element = %d' % (eth, e))


# skip (continue)
for e in lst:
	if e < 0:
		print('continue???')
		continue
	print(e)
'''
