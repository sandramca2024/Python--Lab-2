# set_operations.py

def add_element(s, element):
   # adding elements
    s.add(element)

def remove_element(s, element):
    # removing elements
    s.discard(element)

def union_intersection(set1, set2):
    # union and intersection
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    return union, intersection

def difference(set1, set2):
    # difference
    diff = set1.difference(set2)
    return diff

def is_subset(set1, set2):
    # checking if subset or not
    return set1.issubset(set2)

def set_length(s):
    # length without len()function
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(set1, set2):
    # symmetric difference
    return set1.symmetric_difference(set2)

def power_set(s):
    # power set
    power_set = [[]]
    for element in s:
        power_set += [subset + [element] for subset in power_set]
    return [set(subset) for subset in power_set]

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    s = list(s)  # Convert the set to a list for indexing
    subsets = []
    
    def backtrack(start, current):
        subsets.append(set(current))
        for i in range(start, len(s)):
            backtrack(i + 1, current + [s[i]])
    
    backtrack(0, [])
    return [set(subset) for subset in subsets]
