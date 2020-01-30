# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    print(arr)
    print("Selection sort begins")
    # For all indices EXCEPT the last index:
    print("\n\tinitiate 1st loop to sort each item")
    for i in range(0, len(arr) - 1):
        print(arr)
        print(f"\tSetting current index to {i} where the value is {arr[i]}")
        cur_index = i
        print(
            f"\tSetting smallest index to {cur_index} where the value is {arr[cur_index]}")
        smallest_index = cur_index
        for j in range(cur_index, len(arr)-1):
            print("\n\t\tInitiate nested loop to go find next smallest index")
            print(f"\t\tSetting nested index to {j}")
            nested_index = j
            if arr[nested_index] < arr[smallest_index]:
                print(
                    f"\t\tNested index's value {arr[nested_index]} IS smaller than smallest index's value {arr[smallest_index]}")
                smallest_index = nested_index
                print(
                    f"\n\t\t!! Resetting smallest index to {nested_index} !!")
                print("\t\t\t!!Swapping!!")
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
                print(
                    f"\t\t\t {arr[cur_index]}, {arr[smallest_index]} = {arr[smallest_index]}, {arr[cur_index]}")
            else:
                print(
                    f"\t\tNested index's value {arr[nested_index]} IS NOT smaller than smallest index's value {arr[smallest_index]}")
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #     1. Loop through your array

    for i in arr:
        #     - Compare each element to its neighbor
        #     - If elements in wrong position (relative to each other,
            # swap them)
        # 2. If no swaps performed, stop.
        # Else,
            #   go back to the element at index 0 and repeat step 1.

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


selection_sort([2, 1, 5, 4, 7, 3, 9])
