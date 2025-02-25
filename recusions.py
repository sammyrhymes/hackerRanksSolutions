# fib sequence, starting 0 and 1 
# then add the two previous numbers to get the new one

# start a list with [0,1] 
# first loop do index i + index i+1
# fib_sequnce = [0,1]
# def fib(loops):

#     for loop in range(0,loops-2):
#         fib_sequnce.append(fib_sequnce[loop] + fib_sequnce[loop + 1])
    
#     return print(fib_sequnce)

# fib(18)

# using recusrions
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))
