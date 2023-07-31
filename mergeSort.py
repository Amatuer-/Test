def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        print('left is '+str(left))
        print('right is '+str(right))

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        print(i,j,k)

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                print(f'{left[i]} is lesser than {right[j]}')
                arr[k] = left[i]
                i+=1
            else:
                print(f'{right[j]} is lesser than {left[i]}')
                arr[k] = right[j]
                j+=1
            k+=1

        # while i< len(left):
        #     print(f'{left[i]} was left')
        #     arr[k] = left[i]
        #     i+=1
        #     k+=1
        #
        # while j < len(right):
        #     print(f'{right[j]} was left')
        #     arr[k] = right[j]
        #     j+=1
        #     k+=1
        print(f'{arr} at the end of all while loops')
    return arr

if __name__ == '__main__':
    array = [38, 27, 43, 3, 9, 82, 10]
    print(mergeSort(array))