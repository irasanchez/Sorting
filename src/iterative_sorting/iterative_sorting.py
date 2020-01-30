# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    print(arr)
    print("Selection sort begins")
    # For all indices EXCEPT the last index:
    print("\n\tinitiate 1st loop")
    for i in range(0, len(arr) - 1):
        print(arr)
        # a. Loop through elements on right-hand-side
        # of current index and find the smallest element
        print(f"\tSetting current index to {i} where the value is {arr[i]}")
        cur_index = i  # starts at 0
        print(
            f"\tSetting smallest index to {cur_index} where the value is {arr[cur_index]}")
        smallest_index = cur_index  # this value will change
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # for Loop range(cur_index, length)
        # what is length? the whole list - 1 again?
        for j in range(cur_index, len(arr)-1):
            print("\n\t\tInitiate nested loop")
            # if the nested index is less than the smallest index
            print(f"\t\tSetting nested index to {j}")
            nested_index = j
            if arr[nested_index] < arr[smallest_index]:
                print(
                    f"\t\tNested index's value {arr[nested_index]} IS smaller than smallest index's value {arr[smallest_index]}")
                # smallest_index = nested loop's current index not line 7 index
                smallest_index = nested_index
                print(
                    f"\n\t\t!! Resetting smallest index to {nested_index} !!")
                # array[0] , array[1] = array[1] , array[0]
                print("\t\t\t!!Swapping!!")
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
                print(
                    f"\t\t\t {arr[cur_index]}, {arr[smallest_index]} = {arr[smallest_index]}, {arr[cur_index]}")
            else:
                print(
                    f"\t\tNested index's value {arr[nested_index]} IS NOT smaller than smallest index's value {arr[smallest_index]}")

        # TO-DO: swap
        # b. Swap the element at current index with the
        # smallest element found in above loop
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


selection_sort([2, 1, 5, 4, 7, 3, 9])
