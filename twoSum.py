# given an array and a target, find two numbers in the
# array that sum up to the target 
# e.g
# nums = [4, 7, 2, 11] and the target is 6
# expected answer is [4, 2]

# SOLUTION
# we use hash maps which are dictionaries in python:
# by subracting the number from the target and looking
# up the difference in the hash map we efficiently 
# find the two numbers

def two_sum(nums, target):
    numbers = dict()

    for index, number in enumerate(nums):
        difference = target - number

        if difference in numbers:
            return print([number, difference])
        else:
            numbers[number] = index
    return print("none here!")

two_sum([1,2,3], 4)

