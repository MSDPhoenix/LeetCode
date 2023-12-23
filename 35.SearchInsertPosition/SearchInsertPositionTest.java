class SearchInsertPositionTest {
    public static void main(String[] args){
        SearchInsertPosition search = new SearchInsertPosition();

        int[] nums1 = {1,3,5,6};
        int target1 = 5;

        int[] nums2 = {1,3,5,6};
        int target2 = 2;

        int[] nums3 = {1,3,5,6};
        int target3 = 7;

        System.out.println("A "+search.searchInsert(nums1,target1));
        System.out.println("B "+search.searchInsert(nums2,target2));
        System.out.println("C "+search.searchInsert(nums3,target3));

    }
}
