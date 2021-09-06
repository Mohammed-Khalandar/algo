def isValidSubsequence(array, sequence):
    # Write your code here.
    count = 0
    for value in array:
	    if count == len(sequence):
		    break
	    if sequence[count] == value:
		    count += 1
			
    return count == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array,sequence))