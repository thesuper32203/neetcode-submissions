class Solution {

    public String encode(List<String> strs) {

        String eString = new String();
        for(int i = 0; i<strs.size();i++){
        eString+=strs.get(i).replace(" ", "-") + " ";
        
        }
        return eString;
    }

    public List<String> decode(String str) {
        
        List<String> dString = new ArrayList<>();
        int j = 0;
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i) == ' '){
                dString.add(str.substring(j,i).replace("-", " "));
                j = i+1;
            }
            
        }
        return dString;
    }
}
