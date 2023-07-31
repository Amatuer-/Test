#using library

import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    print(heapq.heapify(arr))
    result = []
    print(heapq.heappop(arr))
    while arr:
        result.append(heapq.heappop(arr))
    return result

#using logic only ; no library


def heapify(arr , n, i):  #(arr , 6, 1)
    count =0

    largest = i # 2nd recurrence mein largest  = 1
    left = 2*i+1  # 2nd recurrence left = 3
    right = (2*i)+2  # 2nd recurrence right = 4

    if left < n and arr[i] < arr[left]: # yes 3 < 6 and arr[1]=20 < arr[3] = 70
        largest = left
        print(f'left loop {largest}')
    if right < n and arr[largest] < arr[right]:
        largest = right
        print(f'right loop {largest}')
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap 1 arr[1] = arr[3] = 70 and arr[largest=3]=20
        print(f'swap block loop {largest}')
        print(arr)
        count += 1
        # Heapify the root.
        heapify(arr, n, largest)

        print(f'{count} recurrence completed')
def heapsort(arr):
    n = len(arr)
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):   # value of corresponding loop 2 , 1,0
        print(f'heapify({arr}, {n}, {i}')
        heapify(arr, n, i)  # 1) heapify(arr , 6 , 2)

    # One by one extract elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        print(f'heapify({arr}, {i}, {0}')
        heapify(arr, i, 0)

if __name__ == '__main__':
    arr = [60, 20, 40, 70, 30, 10]
    # print("Input Array: ", arr)
    # print("Sorted Array: ", heap_sort(arr))
    # Input Array: [60, 20, 40, 70, 30, 10]
    # Sorted Array: [10, 20, 30, 40, 60, 70]
    heapsort(arr)
    n = len(arr)
    print('Sorted array is')
    for i in range(n):
        print(arr[i])
