# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    pass
    # swap_flag = True

    # while swap_flag == True:
    #     swap_flag = False

    #     for i in arr:
    #         # compare to item on RHS
    #         rhs = i+1
    #         if arr[i] > arr[rhs]:
    #             temp = arr[i]
    #             arr[i] = arr[rhs]
    #             arr[rhs] = temp


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


selection_sort([2, 1, 5, 4, 7, 3, 9])
