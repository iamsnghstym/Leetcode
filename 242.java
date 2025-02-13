class Solution {
    public boolean isAnagram(String s, String t) {
        int[] mapper = new int[26];
        for(char ch: s.toCharArray()) {
            int index = ch - 'a';
            mapper[index] += 1;
        }

        for(char ch: t.toCharArray()) {
            int index = ch - 'a';
            mapper[index] -= 1;
        }

        for(int i=0;i<26;i++) {
            if(mapper[i]!=0){
                return false;
            }
        }
        return true;
    }
}