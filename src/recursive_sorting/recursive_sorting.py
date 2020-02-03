# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    print("elements: ", elements)
    merged_arr = [0] * elements
    # TO-DO
    if arrA[0] < arrB[0]:
        merged_arr[0] = arrA[0]
    else:
        merged_arr[0] = arrB[0]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

def merge_sort(arr):
    print("merge sort called for ", arr)
    middle = int(len(arr) / 2)
    print("middle index: ", middle)
    first_half = arr[:middle]
    second_half = arr[middle:]

    if len(first_half) == 1 and len(second_half) == 1:  # base
        # :'s send data as list, not just element

        print(merge(first_half, second_half))

    else:  # recursive case
        print("merge sort first half")
        merge_sort(first_half)  # recurse first half
        print("merge sort second half")
        merge_sort(second_half)  # recurse second half

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
