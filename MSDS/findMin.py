def findMin(a):
    min = a[0]
    for i in a:
        if min > i:
            min = i
    return min

if __name__ == '__main__':
    a = [8,3,9,0,-4,1,2,76,99,55,-2,8]
    print(findMin(a))