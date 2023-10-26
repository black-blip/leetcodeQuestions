class Solution(object):
  def twoSum(self,nums,target):
    '''
    :type nums:List[int]
    :type target: int
    :rtype: List[int]
    '''
    for i,j in enumerate(nums):
      cp = target-j
      if cp in nums and nums.index(cp)!=i:
        return i,nums.index(cp)
