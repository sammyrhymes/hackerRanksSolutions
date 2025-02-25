# an algo where elements are arranged from small to largest
# by comparing two subsequent elements and moving the larger
# to the higher index.


# An array with values to sort.
# An inner loop that goes through the array and swaps values 
# if the first value is higher than the next value. This loop 
# must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop 
# must run. For an array with n values, this outer loop must 
# run n-1 times.


arr = [2,7,4,8,10,2,34,5,6]

n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)