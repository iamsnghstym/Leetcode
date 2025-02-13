class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hashMap = new HashMap<>();
        for(String word: strs) {
            // Sort this word
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            // Check if this sortedWord is in hashMap
            if(hashMap.containsKey(sortedWord)) {
                hashMap.get(sortedWord).add(word);
            } else {
                ArrayList<String> anagrams = new ArrayList<>();
                anagrams.add(word);
                hashMap.put(sortedWord, anagrams);
            }
        }

        // Get all the values from hashMap
        List<List<String>> values = new ArrayList<>(hashMap.values());
        return values;
    }
}