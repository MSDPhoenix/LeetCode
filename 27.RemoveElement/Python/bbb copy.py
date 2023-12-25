nums = [3,2,2,3]
val = 3



def removeElement(nums, val):
    print(nums)
    nums[:] = [x for x in nums if x != val]
    print(nums)
    return len(nums)

print(removeElement(nums,val))