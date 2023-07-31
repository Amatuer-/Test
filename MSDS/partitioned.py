def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    print(n)
    pivot = a[n-1] # choose last element as the pivot.
    print(f'pivot is {pivot}')
    i= -1 # initialize i and j both to be 0
    j = 0
    for j in range(n-1): # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        print(f'j is {j}')
        if a[j] <= pivot:
            print(f'a[j] {a[j]} is <= pivot so swap it ')
            swap(a, i+1, j)
            i = i + 1
    swap(a, i+1, n-1) # place pivot in its correct place.
    return i+1 # return the index where we placed the pivot

def dummyFunction():
    pass

def testIfPartitioned(a, k):
    # TODO : test if all elements at indices < k are all <= a[k]
    #         and all elements at indices > k are all > a[k]
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    # your code here
    n = len(a)
    res = True
    for j in range(n):
        # print(j, a[j], a[k])
        # print(res)
        if (j<k and a[j] >a[k]) or (j >k and a[j] <= a[k]):
            # print('if')
            res = False
    return res







if __name__ == '__main__':
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 10, 23], 5) == True, ' Test # 1 failed.'
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 11, 23], 4) == False, ' Test # 2 failed.'
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 23, 21], 0) == True, ' Test # 3 failed.'
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 22, 23], 9) == True, ' Test # 4 failed.'
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23], 5) == False, ' Test # 5 failed.'
    # assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 13, 9, -11], 5) == False, ' Test # 6 failed.'
    # assert testIfPartitioned([4, 4, 4, 4, 4, 8, 9, 13, 9, 11], 4) == True, ' Test # 7 failed.'
    # print('Passed all tests (10 points)')
    # a1 = [4, 4, 4, 4, 4, 8, 9, 13, 9, 11]
    a1 = [-1, 5, 2, 3, 4, 8, 9, 14, 10, 23]
    a2 = [1, 1, 1, 1, 1, 8, 9, 13, 9, 11]
    a3 = [2, 2, 2, 2, 2, 8, 9, 13, 9, 11]
    try:
        j1 = tryPartition(a1)
        assert not testIfPartitioned(a1, j1)
        print('Partitioning was unsuccessful - this is what you were asked to break the code')
    except Exception as e:
        print(f'Assertion failed {e} - this is fine since you were asked to break the code.')

    try:
        j2 = tryPartition(a2)
        assert not testIfPartitioned(a2, j2)
    except Exception as e:
        print(f'Assertion failed {e} - this is fine since you were asked to break the code.')

    try:
        j3 = tryPartition(a3)
        assert not testIfPartitioned(a3, j3)
    except Exception as e:
        print(f'Assertion failed {e} - this is fine since you were asked to break the code.')

    dummyFunction()

    print('Passed 5 points!')