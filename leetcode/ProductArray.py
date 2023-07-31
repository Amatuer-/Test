def productExceptSelf(nums):
    currProd = 1
    k = 0 #write into nums using k index

    for i in range(len(nums)):
        # i = 0  k=0 24
        #i = 1  
        currProd *= nums[i]
        # kth = currProd//nums[i]
    for k in range(len(nums)):
        kth = currProd//nums[k]
        nums[k] = kth
        k+=1
    return nums

if __name__ == '__main__':
    nums = [1,2,3,4]
    out = productExceptSelf(nums)
    print(out)