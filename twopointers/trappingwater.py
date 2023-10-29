class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0

        if not height:
            return 0

        maxl = height[left]
        maxr = height[right]
        while left<right:

            if height[left]<height[right]:
                left+=1
                maxl = max(maxl,height[left])
                res+=(maxl-height[left])
            
            else:
                right-=1
                maxr = max(maxr,height[right])
                res+=(maxr-height[right])



        return res

            