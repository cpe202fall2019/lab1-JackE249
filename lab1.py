def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError

    max_num = int_list[0]

    for num in int_list:
        if num > max_num:
            max_num = num
    return max_num


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError
    if len(int_list) == 1:
        return [int_list[0]]
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    #checking for edge cases
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError
    if int_list[0] > target:
        return None
    if int_list[len(int_list) - 1] < target:
        return None

    mid = (high - low) // 2
    #binary search
    if int_list[mid] > target:
        low = mid-1
        bin_search(target, low, high, int_list)
    elif int_list[mid] < target:
        high = mid+1
        bin_search(target, low, high, int_list)
    elif int_list[mid] == target:
        return mid
    else:
        return None

    pass
