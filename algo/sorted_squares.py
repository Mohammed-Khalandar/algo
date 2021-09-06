def sortedSquaredArray(array):
    a = [x**2 for x in array]
    a.sort()
    return a


if __name__ == '__main__':
    array = [1, 2, 3, 5, 6, 8, 9]
    print(sortedSquaredArray(array))