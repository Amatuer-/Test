def pivotIndex(nums):
    l = 0
    r = len(nums)
    mid = (l+r)//2
    print(l , r , mid)
    left = nums[l:mid]
    right = nums[mid:r]
    while l < r:
        nums



if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))
