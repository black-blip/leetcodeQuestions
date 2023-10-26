def longestCommonSequence(nums):
    hashset = set(nums) #because duplicate values won't contribute
    count = 0

    for n in hashset:

        if n-1 not in hashset:

            streak = 1

            while n+1 in hashset:
                n = n+1
                streak+=1
            count = max(count,streak)
        

    return count






nums = [100,4,200,1,3,2]
nums1 = [0,3,7,2,5,8,4,6,0,1]


print(longestCommonSequence(nums))
print(longestCommonSequence(nums1))