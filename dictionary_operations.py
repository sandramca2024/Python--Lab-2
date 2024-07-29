def merging_Dict(*args):
    #merge dictionaries into 1
    merged = {}
    for dictionary in args:
        merged.update(dictionary)
    return merged

def common_keys(*args):
    # find common keys 
    if not args:
        return set()
    
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common.intersection_update(dictionary.keys())
    
    return common

def invert_dict(dictionary):
    #invert a dictionary and sway keys and values
    inverted = {}
    for key, value in dictionary.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

def common_key_value_pairs(*args):
    #find common key value pairs
    if not args:
        return set()
    
    common_pairs = set(args[0].items())
    for dictionary in args[1:]:
        common_pairs.intersection_update(dictionary.items())
    
    return common_pairs
