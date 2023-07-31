def twoWayMerge(lst1, lst2):
    # Implement the two way merge algorithm on
    #          two ascending order sorted lists
    # return a fresh ascending order sorted list that
    #          merges lst1 and lst2
    i, j = 0, 0

    merged_list = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            merged_list.append(lst2[j])
            j += 1
        else:
            merged_list.append(lst1[i])
            i += 1

    if i < len(lst1):
        merged_list += lst1[i:]

    if j < len(lst2):
        merged_list += lst2[j:]

    return merged_list

def oneStepKWayMerge(list_of_lists):
    if (len(list_of_lists) <= 1):
        return list_of_lists
    ret_list_of_lists = []
    k = len(list_of_lists)
    # print(k)
    for i in range(0, k, 2):
        if (i < k - 1):
            ret_list_of_lists.append(twoWayMerge(list_of_lists[i], list_of_lists[i + 1]))
        else:
            ret_list_of_lists.append(list_of_lists[k - 1])
    return ret_list_of_lists

def kWayMerge(list_of_lists):
    k = len(list_of_lists)
    # print(k)
    if k == 1:
        return list_of_lists[0]
    else:
        new_list_of_lists = oneStepKWayMerge(list_of_lists)
        return kWayMerge(new_list_of_lists)

if __name__ == '__main__':
    print(kWayMerge([[1,2,3], [4,5,7],[-2,0,6]]))