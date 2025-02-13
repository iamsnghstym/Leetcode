class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        Set<Integer> numsSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        for(Integer num: numsSet) {
            int length = 0;

            // Does it qualify to be the start of the sequence
            if(!numsSet.contains(num-1)) {
                while(numsSet.contains(num + length)) {
                    length += 1;
                }

                max = Math.max(max, length);
            }
        }

        return max;
    }
}