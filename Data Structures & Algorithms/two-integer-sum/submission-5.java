class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int compl = 0;
        Map<Integer,Integer> numMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++)
        {
            int num = nums[i];
            compl = target - num;

            if(numMap.containsKey(compl)){
                result[1] = i;
                result[0] = numMap.get(compl);
                return result;
            }

            numMap.put(num,i);

        }
        return new int[]{};
    }
}
