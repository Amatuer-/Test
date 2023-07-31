def mergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0

        while i < len(left) and j< len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i+=1
            else:
                a[k] = right[j]
                j+=1
            k+=1
        while i< len(left):
            print(f'{left[i]} was left')
            a[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            print(f'{right[j]} was left')
            a[k] = right[j]
            j+=1
            k+=1
        return a






if __name__ == '__main__':
    array = [38, 27, 43, 3, 9, 82, 10]
    print(mergeSort(array))