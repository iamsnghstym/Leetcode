class Solution {
    public int majorityElement(int[] nums) {
        int candidate = -1;
        int votes = 0;

        for(int num: nums) {
            if(votes == 0) {
                candidate = num;
                votes = 1;
            } else {
                if(num == candidate) {
                    votes += 1;
                } else {
                    votes -= 1;
                }
            }
        }

        // System.out.println(candidate);

        // Check if candidate is the majority element
        int count = 0;
        for(int i=0;i<nums.length;i++) {
            if(nums[i] == candidate) {
                count += 1;
            }
        }

        if (count > nums.length / 2) {
            return candidate;
        } else {
            return -1;
        }
    }
}