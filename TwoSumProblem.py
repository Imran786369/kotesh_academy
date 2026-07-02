def twoSum(nums, target):
    num_map = {}  # Stores number as key and its index as value

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i

# Example 1
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

# Example 2
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]

# Example 3
nums = [3, 3]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]