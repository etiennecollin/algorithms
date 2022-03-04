# For understanding only
# def quicksort(array):
# 	head = []
# 	equal = []
# 	tail = []
	
# 	if len(array) > 1:
# 		pivot = array[0]
# 		for value in array:
# 			if value < pivot:
# 				head.append(value)
# 			elif value > pivot:
# 				tail.append(value)
# 			else:
# 				equal.append(value)	
# 		return quicksort(head)+equal+quicksort(tail)
# 	else:
# 		return array

def quicksort(array):
    if not array: return array # empty sequence case
    pivot = array[0]

    head = quicksort([value for value in array if value < pivot])
    tail = quicksort([value for value in array if value > pivot])
    return head + [value for value in array if value == pivot] + tail

# Iterative

# For singly linked list

# For doubly linked list

# 3-way