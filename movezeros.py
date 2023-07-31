def moveZeroes(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] !=0:
            nums[i] , nums[j] = nums[j] , nums[i]
            i +=1
    return nums





if __name__ == '__main__':
    print(moveZeroes([1,0,2,0,3]))