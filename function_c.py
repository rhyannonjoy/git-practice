def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    list_a_set = set(list_a)
    list_b_set = set(list_b)
    merged_sets = list_a_set.union(list_b_set)
    merged_lists = list(merged_sets)
    return merged_lists


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
