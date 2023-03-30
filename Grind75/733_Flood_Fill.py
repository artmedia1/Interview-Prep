from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        xlen = len(image)
        ylen = len(image[0])
        original = image[sr][sc]
        
        def dfs(x, y):
            if 0<=x<xlen and 0<=y<ylen and image[x][y]==original:
                image[x][y] = color
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)

        if original != color:
            dfs(sr,sc)
        
        return image
      
if __name__ == "__main__":        
    solution = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    test = solution.floodFill(image, sr, sc, color)
    print(test)
