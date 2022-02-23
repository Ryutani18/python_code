def permute(nums, m=0):
    nums.sort() if m == 0 else nums
    if len(nums) == 1:
        return [nums]
    li = []
    temp = int
    for i in range(len(nums)):
        if nums[i] == temp:
            continue
        array = permute(nums[:i] + nums[i+1:], m+1)
        for arr in array:
            arr.insert(0,nums[i])
        li += array
        temp = nums[i]
    return li

array = [1,2,3,4,5]
print(permute(array))