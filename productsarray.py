def productExceptSelf(nums):
    i = 0
    j = 0
    k = 0 # nums[k]
    prod = 1
    while i < len(nums):
        # print(nums[i] , nums[i+1:])
        res = product(nums[i+1:])
        i += 1
        print(res)
        # nums[k] = res
    # return nums

def product(a):
    p = 1
    for i in range(len(a)):
        # print(a[i])
        p = p*a[i]
    return p

if __name__ == '__main__':
    res = productExceptSelf([1,2,3,4]) #[24,12,8,6]
    print(res)
    # product(a=[1,2,3,4])
    # a[0] = a[1]*a[2]*a[3]
    # a[1] = a[0]*a[2]*a[3]
    # a[2] = a[0]*a[1]*a[3]
    # a[3] = a[0]*a[1]*a[2]