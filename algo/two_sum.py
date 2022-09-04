def two_sum(nums,target):
#     for i in array:
#         diff = targetSum -i
#         if diff != i and diff in array:
#             return [diff,i]
#     return []
# Solution 1
    for i in range(len(nums)):
        diff = target - nums[i]
        nums[i] = None
        if  diff in nums:
            return ([i,nums.index(diff)])
#Solution 2
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        nums[i] = None
        if remaining in nums:
            return [i, nums.index(remaining)]
        
if __name__ == '__main__':
    nums = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    print(two_sum(nums,target))
