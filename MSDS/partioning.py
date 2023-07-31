def partition(arr):
    #select the pivot
    n = len(arr)
    pivot = arr[n-1]
    # print(x)#8
    i = -1
    j = 0
    for j in range(n-1):
        if arr[j] <= pivot:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i +=1
    arr[i+1] , arr[n-1] = arr[n-1], arr[i+1]
    print(arr)




if __name__ == '__main__':
    arr = [4,3,2,1]
        #[2,1,3,7,4,6,5,9,8]
    print(partition(arr))