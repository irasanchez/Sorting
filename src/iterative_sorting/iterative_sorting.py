# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # For all indices EXCEPT the last index:
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)-1):
            nested_index = j
            if arr[nested_index] < arr[smallest_index]:

                smallest_index = nested_index

                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

            else:

    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     #     1. Loop through your array

#     for i in arr:
#         #     - Compare each element to its neighbor
#         #     - If elements in wrong position (relative to each other,
#             # swap them)
#         # 2. If no swaps performed, stop.
#         # Else,
#             #   go back to the element at index 0 and repeat step 1.

#     return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


selection_sort([2, 1, 5, 4, 7, 3, 9])
