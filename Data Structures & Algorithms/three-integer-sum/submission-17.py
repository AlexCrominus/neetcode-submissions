class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)


        ret = []
        print(nums)
        for i in range(len(nums)):
            l,r = 0, len(nums)-1 
            while l<r:
                sum3 = nums[i] + nums[l] + nums[r]
                # print(sum3, nums[l], nums[i], nums[r])
                
                if sum3 == 0 and sorted([nums[i], nums[l], nums[r]]) not in ret and l!=i and i!=r and l!=r:
                    ret.append(sorted([nums[i], nums[l], nums[r]]))
                    r-=1
                    l+=1
                elif sum3 > 0:
                    r-=1 
                else:
                    l+=1
            
            # if not (l % 2) :
            #     l+=1
            # else:
            #     r-=1 

        return ret

