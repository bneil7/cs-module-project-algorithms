'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # array cannot be empty
    # all values in array are repeated, except for one
    # check every element in the array
    # after every iteration of checking the array, keep track of the value being checked
    # confirm if current value is repeated anywhere else in the array
    # return the only value that had no repeats

    # loop thru the array with range
    for i in range(len(arr) - 1):
        # store reference of frequency of i's repitition in array
        found_value = 1
        # nested for loop, looping through the length of the array
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                # increment by 1
                found_value += 1
        # if inner loop fully runs, and found_value is still == 1, then i is the correct answer
        if found_value == 1:
            result = arr[i]
            return result


test_arr = [1, 2, 1, 2, 4]
print(single_number(test_arr))


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")
