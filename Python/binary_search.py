def binary_search(input, target):
	low = 0
	mid = 0
	high = len(input)-1

	while low<= high:
		mid = int((low+high)/2)

		if input[mid] == target:
			return mid
		elif input[mid] < target:
			low = mid+1
		else:
			high = mid-1
	return -1

# Recursive version: Not efficient
# def binary_search_recursive(input, low, high,  target):
# 	if low <= high:
# 		mid = int((low+high)/2)

# 		if input[mid] == target:
# 			return mid
# 		elif input[mid] < target:
# 			return binary_search_recursive(input, mid+1, high, target)
# 		else:
# 			return binary_search_recursive(input, low, mid - 1, target)
# 	else:
# 		return -1