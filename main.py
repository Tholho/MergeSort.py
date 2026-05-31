import sys

unsorted_list = [int(x) for x in sys.argv[1:]]


def split_and_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        middle = len(unsorted_list) - len(unsorted_list) // 2
        first_half = split_and_sort(unsorted_list[:middle])
        second_half = split_and_sort(unsorted_list[middle:]) 

    return fuse_sort(first_half, second_half)


def fuse_sort(listA, listB):
    i = 0
    j = 0
    fused_list = []
    while i < len(listA) and j < len(listB):
        if listA[i] <= listB[j]:
            fused_list.append(listA[i])
            i += 1
        else:
            fused_list.append(listB[j])
            j += 1
    
    fused_list.extend(listA[i:])
    fused_list.extend(listB[j:])
    return fused_list


print(split_and_sort(unsorted_list))