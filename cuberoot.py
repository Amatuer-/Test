def integerCubeRootHelper(n, left, right):
    cube = lambda x: x * x * x # anonymous function to cube a number
    # assert(n >= 1)
    # assert(left < right)
    # assert(left >= 0)
    # assert(right < n)
    # assert(cube(left) < n), f'{left}, {right}'
    # assert(cube(right) > n), f'{left}, {right}'
    mid = (left+right)//2
    print(mid)
    while mid!=left and cube(mid) !=n:
        if cube(mid) >n:
            right = mid
        else:
            left = mid
        mid = (left+right)//2
    return mid




def integerCubeRoot(n):
    # assert( n > 0)
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return integerCubeRootHelper(n, 0, n-1)

if __name__ == '__main__':
    print(integerCubeRoot(26))