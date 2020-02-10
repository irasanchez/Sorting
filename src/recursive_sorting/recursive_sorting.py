# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    print("elements: ", elements)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(merged_arr):
        if len(arrA) == 0:
            # copy rhs to merged_arr
            # merged_arr[i:] = arrB[]
            # if rhs is empty
        if len(arrB) == 0:
            pass
            # copy lhs to merged_arr
        # arrA[0] < arrB[0]:
        merged_arr[i] = arrA[0]
        arrA.pop(0)
        # arrB[0] < arrA[0]
        merged_arr[i] = arrB[0]
        arrB.pop(0)


def merge_sort(arr):
    if len(arr) > 1:
        lhs = merge_sort(arr[:len(arr)//2])
        rhs = merge_sort(arr[len(arr)//2:])
        merge(lhs, rhs)

    return arr


merge_sort([3, 2, 1, 6, 4, 5, 8])

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
        # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
