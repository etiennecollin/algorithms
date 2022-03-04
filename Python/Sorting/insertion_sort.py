def insertion_sort(array):
	for i in range(1, len(array)):
		currentValue = array[i]
		currentPosition = i

		while currentPosition > 0 and array[currentPosition - 1] > currentValue:
			array[currentPosition] = array[currentPosition -1]
			currentPosition -= 1
		
		array[currentPosition] = currentValue
	return array

# Recursive