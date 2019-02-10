# Program to create a list consisting of an arithmetic sequence starting at 1 with a common difference of 3,
# using a for loop.

# The final output is expected to be like this:
# [1, 4, 7, 10, 13, 16, 19, 22, 25]
# If the first term is represented by a and the common difference is represented by d
# and the number of terms is represented by n, then the entire arithmetic sequence can be represented as:
#            [a, a + d, a + 2d, a + 3d, a + 4d, ..., a + (n-1)d] where a is unchanged from beginning to end.
# index:      0    1      2       3       4     ...   n-1

# Initialize the list variable that is used to store the arithmetic sequence, the variable representing term/element,
# the common difference (counter) and the number of terms in this sequence.
seq = []    # The list to store the arithmetic sequence.
a = 1   # The term variable.
d = 3   # The common difference.
n = int(input("How many terms do you want? "))   # The number of terms in this sequence.
for i in range(n):
    a = 1 + i * d
    # a = 1 + 0 * 3 = 1
    # a = 1 + 1 * 3 = 4
    # a = 1 + 2 * 3 = 7
    # a = 1 + 3 * 3 = 10
    # ...
    seq.append(a)
print(seq)


'''This is my first GitHub demo.'''
