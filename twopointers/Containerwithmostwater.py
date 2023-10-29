class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = []
        
        def twoSum(i,target):
            
            j = len(nums)-1

            while i<j:

                if nums[i]+nums[j]+target==0:
                    ans.append([target,nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    
                
                elif nums[i]+nums[j]+target>0:
                    j-=1
                
                else:
                    i+=1
        

        for i,num in enumerate(nums):
            
            if num>0:
                break
            
            if i>0 and num==nums[i-1]:
                continue
            
            twoSum(i+1,num)

            
        return ans