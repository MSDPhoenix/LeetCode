const nums1 = [1,3,5,6]
const target1 = 5

const nums2 = [1,3,5,6]
const target2 = 2

const nums3 = [1,3,5,6]
const target3 = 7

function searchInsert(nums,target){
    for(i=0;i<nums.length;i++){
        if(target<=nums[i])
            return i
    }
    return nums.length
}

console.log(searchInsert(nums1,target1))
console.log(searchInsert(nums2,target2))
console.log(searchInsert(nums3,target3))

