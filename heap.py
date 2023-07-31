import heapq


def swap(a,b):
    a, b = b,a
    print(f'{a} was swapped with {b} and viceversa')


if __name__ == '__main__':
    heap = []
    items = [5,5,8,10,9,14,15,11,13,10,11,7]
    for j in range(1, len(items)):
        if items[j] < items[j//2]:
            print(items[j])
            swap(items[j], items[j//2])

        else:
            print('this is a min heap')
    print(items)

    ####implementation using heap function
            # for i in items:
            #     heapq.heappush(heap, i)
            # print('Heap obtained from heappush() : ', heap)
            #
            # heapq.heapify(items)  # transforms list into a heap, in-place, in linear time
            #
            # print('Heap obtained from heapify() : ', items)

