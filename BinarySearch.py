def binarySearchHelper(lst ,elt,left, right):
    # the array should be in sorted order before the search begins
    if left > right:
        return None
    else:
        mid = (left+right)//2
        if elt == lst[mid]:
            return mid
        elif elt < lst[mid]:
            return binarySearchHelper(lst, elt , left , mid-1)

        else:
            return binarySearchHelper(lst , elt , mid+1 , right)




if __name__ == '__main__':
    lst = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    elt = 23
    result = binarySearchHelper(lst ,elt,0, len(lst)-1)
    print(result)