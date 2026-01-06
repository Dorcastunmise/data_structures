def merge_sort(list):
    """
    sorts a list in ascending order
    returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(kn log n) time i.e linearithmic time
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right 

    Takes overall O(k log n) time i.e logarithmic time k being the time taken to split the list
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list O(n)
    """ 

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged   

def verify_sorted(list):
    """
    Helper function to verify if a list is sorted
    Returns True if sorted, False otherwise 
    """

    n = len(list)

    if n == 0 or n == 1: #ie naively sorted
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])


if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print("Unsorted list:", alist)
    sorted_list = merge_sort(alist)
    print("Sorted list:", sorted_list)
    print("Is the list sorted?", verify_sorted(sorted_list))