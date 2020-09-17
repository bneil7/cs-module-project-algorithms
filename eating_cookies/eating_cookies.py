'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # can only eat 1, 2, or 3 cookies at a time
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    # call eating cookies on the numbers 1, 2, and 3 less than our initial N once we hit our first non-base case value of 3+
    #   (base case <= 2)
    elif n >= 3:
        # USING RECURRRRRRRRRRJ
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 30

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
