class Solution {
    // O(nlogn) + O(m*n) = O(m*n)
    public String longestCommonPrefix(String[] strs) {
        StringBuilder lcp = new StringBuilder();
        // O(nlogn)
        Arrays.sort(strs, (a,b) -> Integer.compare(a.length(), b.length()));

        String baseString = strs[0];
        Boolean isLcpFound = true;
        for(int i=0;i<baseString.length();i++) {
            char character = baseString.charAt(i);
            for(int j=1;j<strs.length;j++) {
                if(character != strs[j].charAt(i)) {
                    isLcpFound = false;
                    break;
                }
            }
            if(isLcpFound) {
                lcp.append(character);
            }
        }

        return lcp.toString();
    }
}