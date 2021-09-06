def two_sum(array,targetSum):
    for i in array:
        diff = targetSum -i
        if diff != i and diff in array:
            return [diff,i]
    return []

if __name__ == '__main__':
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(two_sum(array,targetSum))