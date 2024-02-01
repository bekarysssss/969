def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
        pass    
    return False

numbers = [1, 2, 4, 0, 0, 7, 5]
result = spy_game(numbers)
print(result)