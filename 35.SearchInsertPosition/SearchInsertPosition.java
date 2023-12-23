class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        for(int i = 0; i<nums.length; i++){
            System.out.print(""+i+" "+nums[i]+" "+target+"\n");
            if(target<=nums[i]){
                return i;
            }
        }
        return nums.length;
    }
}
