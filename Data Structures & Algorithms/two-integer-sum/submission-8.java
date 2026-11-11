class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Hashtable<Integer,Integer> ht = new Hashtable<>();

        for(int i = 0;i<nums.length;i++){
            ht.put(nums[i],i);
        }
        for(int i = 0;i<nums.length;i++){
            int comp = target - nums[i];
            if(ht.containsKey(comp) &&ht.get(comp)!= i )
            return new int[]{i,ht.get(comp)};
        }
        return new int[]{};
    }
}
