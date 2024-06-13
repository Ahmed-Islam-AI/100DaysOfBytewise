def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

arr1 = [2, 3, 5]
arr2 = [1, 4, 6]
print(merge_sorted_arrays(arr1, arr2))