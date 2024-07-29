# module_ListFunction.py

def find_max(lst):
    #maximum function
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def find_min(lst):
    #minimum function
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def calculate_sum(lst):
    #sum of all elements
    return sum(lst)

def compute_average(lst):
    #average of the elements
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)

def find_median(lst):
    #median of the elements
    if not lst:
        raise ValueError("List is empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_lst[middle - 1] + sorted_lst[middle]) / 2
    else:
        return sorted_lst[middle]
