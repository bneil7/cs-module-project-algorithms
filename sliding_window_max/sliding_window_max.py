'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# what if k is larger than the array ( len(nums) ) ?
#   -- Go with a reasonable interpretation, and then follow through with it in your implementation..
# if k > len(nums), then we'll find the overall max value of the nums array

# does the return array need to be sorted?
#   -- NO, since the prompt didn't specifically say so..


def sliding_window_max(nums, k):
    # loop thru array with range
    # hold max values in empty array
    # check if the index + k will exceed array length
    # reset the max value

    # loop through window (while loop)
    # check if index value is higher than max value

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
