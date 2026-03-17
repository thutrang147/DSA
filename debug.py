def twoSum(nums: list[int], target: int):
    current = []
    for i in range(len(nums)):
        current.append(target - nums[i])
    ans = []
    k = 0
    while k < len(nums):
        for i in range(len(current)):
            if nums[k] == current[i]:
                ans.append([k, i])
        
    return current

print(twoSum([3, 2, 4], 6))
