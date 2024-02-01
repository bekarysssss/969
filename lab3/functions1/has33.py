def has_33(nums):
    pass
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

numbers = [1, 3, 3]
result = has_33(numbers)
print(result)