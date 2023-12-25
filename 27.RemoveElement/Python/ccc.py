nums = [3,2,1,3]
val = 3



def removeElement(nums, val):
    i = 0
    for x in nums:
        print()
        print(i)
        print(x)
        print(nums[i])
        print(nums)
        if x != val:
            print("*")
            nums[i]=x
            print(nums[i])
            i += 1
            print(i)
            print(nums)    
    nums = nums[:i]
    print("\n",nums)
    return i
    

print(removeElement(nums,val))