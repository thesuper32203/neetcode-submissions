class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> sum = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if(sum.containsKey(diff)){
                return new int[]{sum.get(diff),i};
            }
            sum.put(num,i);
        }

        return new int[]{};
    }
}
