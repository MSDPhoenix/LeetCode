
var removeElement = function(nums, val) {
    let i = 0;
    // for (let x = 0; x< nums.length; x++){
    for (x in nums){
        if (nums[x] != val){
            console.log(nums[x])
            nums[i] = nums[x];
            i += 1;
        }
    }
    return i;
}