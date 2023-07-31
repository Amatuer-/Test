def findMaxAverageHelper(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum



def findMaxAverage(nums , k):  #k=4 & [1,12,-5,-6,50,3]
    # Initialize currSum and maxSum to the sum of the initial k elements
    currSum = maxSum = sum(nums[:k])  #sum(1+12+(-5)+(-6))=2
    print(f'currentsum and maxSum initially is {currSum,maxSum}')

    for i in range(k , len(nums)):  # for i in range(4,6)
        print(nums[i], k) #1) nums[4] = 50 and k=4;  2) nums[5] =3 k=4
        print(nums[i],nums[i-k]) #nums[4] = 50 and nums[4-4]=nums[0]=1  ; 2) nums[3]=3 and nums[5-4]=12
        currSum += nums[i]-nums[i-k]  #1) 2+50-1=51  2) 51+3-12=42

        maxSum = max(currSum,maxSum) #1) maxSum = 51 2) maxSum=51
    # Since the problem requires average,  we return the average
    return maxSum / k  #51/4=12.75

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    out = findMaxAverage(nums, k)
    print(out)