class Solution {
    public int[] productExceptSelf(int[] nums) {
         int pre[]=new int[nums.length];
         int post[]=new int[nums.length];
         pre[0]=nums[0]; 
         post[nums.length-1]=nums[nums.length-1];
         for(int i=1;i<nums.length;i++){
            pre[i]=pre[i-1]*nums[i];
         }
         for(int i=nums.length-2;i>=0;i--){
            post[i]=post[i+1]*nums[i];
         }
         int ans[]=new int[nums.length];
         ans[0]=post[1];
         ans[ans.length-1]=pre[ans.length-2];
         for(int i=1;i<nums.length-1;i++){
            ans[i]=pre[i-1]*post[i+1];
         }
         return ans;
    }
}  
