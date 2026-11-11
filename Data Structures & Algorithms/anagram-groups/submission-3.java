class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String,List<String>> h = new HashMap<>();

        for(String s : strs){
            int[] a = new int[26];
            for(char c : s.toCharArray()){
                a[c-'a']++;
            }
            String key = Arrays.toString(a);
            h.putIfAbsent(key,new ArrayList<>());
            h.get(key).add(s);
            
        }

           return new ArrayList<>(h.values());

    }
}
