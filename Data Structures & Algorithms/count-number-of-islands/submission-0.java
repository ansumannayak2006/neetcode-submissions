class Solution {
    public int numIslands(char[][] grid) {
        int grid1[][]=new int[grid.length][grid[0].length];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1'){
                    grid1[i][j]=1;
                }else{
                    grid1[i][j]=0;
                }
            }
        }
        int ans=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid1[i][j]==1){
                    ans++;
                    check(grid1,i,j);
                }
            }
        }
        return ans;
    }
    static void check(int arr[][],int r,int c){
        int pair[][]={{0,-1},{-1,0},{0,1},{1,0}};
        arr[r][c]=0;
        for(int p[]:pair){
            int i=r+p[0];
            int j=c+p[1];
            if(safe(i,j,arr)){
                check(arr,i,j);
            }
        }
    }
    static boolean safe(int r,int c,int arr[][]){
        return r>=0 && r<arr.length && c>=0 && c<arr[0].length && arr[r][c]==1;
    }
}
