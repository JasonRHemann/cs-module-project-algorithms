'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # create new empty array
    new_array = []
    # check if item in array is in new array, if not add it.
    for i in arr:
        if i not in new_array:
            new_array.append(i)
            # if item is in new array remove it leaving only non-duplicate numbers
        else:
            new_array.remove(i)
    return new_array.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
