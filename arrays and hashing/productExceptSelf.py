'''
We cannot use division operation

In this approach, we take the product of every element before the current element and store it in ans and prefix variable. 

We then take the product of every element after the current element and then multiply with the prefix product

'''





def productExceptSelf(nums):
    ans = [1 for _ in range(len(nums))]
    prefix, postfix = 1,1

    for i in range(len(nums)):
        ans[i] = prefix
        prefix = prefix * nums[i]

    for i in range(len(nums)-1,-1,-1):
        ans[i] = ans[i]*postfix
        postfix = postfix*nums[i]

    return ans


nums = [1,2,3,4]

print(productExceptSelf(nums))