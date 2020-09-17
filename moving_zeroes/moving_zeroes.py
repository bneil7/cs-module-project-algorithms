'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # loop thru the array with range
    # check for zero
    # if zero, remove it and append to the right side of the array
    # else, remove it and append to left

    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.insert(len(arr) - 1, 0)
        else:
            num = arr.pop(i)
            arr.insert(0, num)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
