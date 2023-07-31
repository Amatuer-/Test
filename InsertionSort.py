def insertionSort(arr):
    for i in range(1 , len(arr)):
        key = arr[i]
        j = i -1
        while  j >=0 and key < arr[j]:
            arr[j+1] = arr[j] #arr[i-1+1] = arr[i-1] ==> arr[i] = 11
            j-=1
        arr[j+1] = key
    return arr



if __name__ == '__main__':
    inArray = [12,11,13,5,6]
    # [11,12,13,5,6]
    #[ 11,12,13,5,6]
    #[11,12,5,13,6]
    #[
    print(insertionSort(inArray))