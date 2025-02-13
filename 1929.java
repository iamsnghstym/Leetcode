class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length;

        if(length == 0) {
            return nums;
        }

        int[] answer = new int[2*length];

        // O(n) TC
        for(int i=0;i<length;i++) {
            answer[i] = nums[i];
            answer[i+length] = nums[i];
        }
        return answer;
    }
}