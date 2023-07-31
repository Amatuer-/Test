def quickSort(arr, p , r):
    # partitioning portion
    #pivot value is
    x = arr[len(arr)-1]
    print(x)
    i = p-1
    j = p
    while j < r-1:
        if arr[j] <= x:
            i += 1
            j += 1
            arr[i+1], arr[j] = arr[j] , arr[i+1]
    arr[i+1] , arr[r] = arr[r], arr[i+1]
    print(arr)



if __name__ == '__main__':
    arr = [4 ,2,1,9,3,-1,7]
    print(quickSort(arr ,0 , len(arr) ))