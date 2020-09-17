'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # create new array, make it equal to the number of indexes in the given array
    array_length = len(arr)
    new_array = [0] * array_length
    # make a counter (initialize at zero)
    counter = 0

    # loop thru with range
    # for loop, start at the index in front of current index
    for i in range(len(arr)):
        item = 1
        for j in range(len(arr)):
            if j != i:
                # multiply all the numbers in the second for loop
                item = item * arr[j]

         # return that number and insert it into the created array at index of counter
        new_array[counter] = item
        # increment counter += 1
        counter += 1
    return new_array


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # returns "Output of product_of_all_other_numbers: [120, 60, 40, 30, 24]"

    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
