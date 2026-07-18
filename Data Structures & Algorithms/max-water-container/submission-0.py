class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights)-1 
        maxProd = 0
        # max1, max2 = 0,0
        while l<r:
            localMax = min(heights[l], heights[r]) * (r-l)
            # localMax  = min(heights[l], heights[r]) * min(heights[l], heights[r]) 

            if localMax > maxProd:
                maxProd = localMax
            
            # if heights[r] > max1:
            #     max1 = heights[r]

            # if heights[l] > max2:
            #     max2 = heights[l]

            # l+=1 
            # r-=1 

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return maxProd