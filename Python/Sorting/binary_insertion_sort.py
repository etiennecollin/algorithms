def binarySearch(input, target, high = None):
	low = 0
	if high is None:
		high = len(input)-1
	
	while low < high:
		mid = int((low+high)/2)

		if input[mid] <= target:
			low = mid + 1
		else:
			high = mid
	return low

def binaryInsertionSort(array):
	for i in range(1, len(array)):
		currentValue = array[i]
		expectedPosition = binarySearch(array, currentValue, i)
		currentPosition = i

		while currentPosition>expectedPosition:
			array[currentPosition] = array[currentPosition-1]
			currentPosition -= 1
		
		array[expectedPosition] = currentValue
	
	return array