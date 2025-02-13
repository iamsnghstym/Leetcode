class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numsSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        if(numsSet.size() != nums.length) {
            return true;
        }
        return false;
    }
}