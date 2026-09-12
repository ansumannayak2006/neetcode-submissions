 
class Solution {
    public int[] twoSum(int[] numbers, int target) { 
        Map<Integer, List<Integer>> h = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) { 
            if (!h.containsKey(numbers[i])) {
                h.put(numbers[i], new ArrayList<>());
            } 
            h.get(numbers[i]).add(i);
        }
         
        for (int i = 0; i < numbers.length; i++) {
            int t = target - numbers[i];
            
            if (h.containsKey(t)) {
                List<Integer> l1 = h.get(t);
                for (int idx : l1) { 
                    if (idx != i) { 
                        return new int[]{i + 1, idx + 1};
                    }
                }
            }
        }
        
        return new int[]{-1, -1};
    }
}
