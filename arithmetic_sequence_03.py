# Program to sum all the terms in an arithmetic sequence starting at "a" with a common difference of "d".
# using a for loop.

# If we initialize (assign an initial value to) the variable that is to store the sum of the arithmetic sequence.
seq_sum = 0  # Any sequence sum should start at zero even if the sequence starts at zero.

# To work out the final sum, we need a changing counter. When referring to "counter", I mean a stuff that looks like,
# say, triangle-shaped teaching tool, for teaching children how to do an addition. Each counter is actually an term in
# a sequence, the first and smallest term is, for example, 1, the second term is 4, the third term is 7,
# the fourth term is 10, and then 13, 16, 19, 22, 25, 28, etc.
# Therefore, when we initialize the counter, we should assign the value of the first term to the first counter - a.
a = int(input("Enter your first term: "))


# Initialize the common difference which is shorten as "d".
d = int(input("Enter the common difference: "))

# Technically, an arithmetic sequence can be infinite.
# What we really need in reality, however, must be a finite sequence.
# Therefore, we need to set a finite number of terms. In a program, we need to ask users for that number.
n = int(input("How many terms do you want? "))

# For add a new item (here, term) to the list of number sequence one at a time, we need to initialize the sequence list
# as am empty list.
seq_ls = []

for n in range(1, n + 1):
    # Mathematically, each term in an arithmetic sequence can be represented as: a + (n - 1)d, where n is the number of
    # terms. To make sure n is a positive integer to store a value from 1 up to n (n is included here), we need to make
    # the "stop" part in the range(start, stop[, step]) function 1 greater than n, since the value of the "stop" is not
    # included in the list of the range. For example, list(range(1, 5) refers to [1, 2, 3, 4] where 5 is excluded
    # according to Python docs.
    counter = a + (n - 1) * d
    seq_sum = seq_sum + counter
    seq_ls.append(counter)
print(f"\nThe arithmetic sequence is: {seq_ls}")
print(f"\nThe sum of the sequence is: {seq_sum}")
