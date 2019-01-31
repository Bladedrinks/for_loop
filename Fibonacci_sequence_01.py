# Program to create a list of the Fibonacci sequence where we ask the user for the first two terms,
# using for loop.

# n  = ... -6  -5  -4  -3  -2  -1	0	1	2	3	4	5	6   7	8	9	10	11	12	13	14	15	...

# Xn = ... -8	5  -3	2  -1	1	0	1	1	2	3	5	8   13	21	34	55	89	144	233	377	610	...

# Initialize the first two terms and the number of terms in this Fibonacci sequence.
a = int(input("Enter the first term: "))
b = int(input("Enter the second term: "))
Fb_seq = [a, b]
# The most commonly seen Fibonacci sequence begins at 0 and 1 or 1 and 1. Actually, we have more choices at this point.
# We can use any two random integers to begin a Fibonacci-like sequence, like 192 and 16. Therefore, the sequence looks
# like this: 192, 16, 208, 224, 432, 656, 1088, 1744, 2832, 4576, 7408, 11984, 19392, 31376, ...

# index:  0  1  2  ...
n = int(input("Enter the number of terms: "))

# To obtain the indices of the two terms in the rule, we need to reference a for loop.
for i in range(2, n):
    x = Fb_seq[i-1] + Fb_seq[i-2]
    # This is the core code in the program and the jumping-off point of the program design,
    # because it is the rule of the Fibonacci sequence,
    # which says that each succeeding term in the sequence is the sum of the two immediately preceding.
    # Mathematically, if we let the ordinal number of the Fibonacci sequence be n and any succeeding term X,
    # then we can write the rule: X(n) = X(n-1) + X(n-2), where X(n) is Term n, X(n-1) is the term right before Term n,
    # and X(n-2) is the term right before Term n-1.
    # The next question is: Since n should change until we want it to stop at some number, how to assign a value to the
    # variable n one at a time.
    # The Fibonacci sequence has a unique feature comparing to other sequences, which is each term is the sum of the two
    # terms right before it. The challenging issue is these two preceding terms are unstable. The only stable terms are
    # the first two terms which need to be set by users. The Fibonacci sequence is fundamentally a list of integers.
    # Now that the sequence is also a list, in a list every item has its own unique index from 0 up to n-1. So if there
    # is a term whose index is i, then naturally the two terms right before it have indices i-1 and i-2.
    # This relationship can be written as: list[i] = list[i-1] + list[i-2].
    # For keeping getting a new value of i, we need to use a for loop to pick a new value from a range of values.
    # For now, we might need to think about the start, stop and step size of the range. In other words, the range should
    # be from what up to, but not including, what?
    # As I said before, the very first two terms of the Fibonacci sequence have been set at the very beginning, so the
    # list of the sequence is not an empty list like other number sequence. The list or the initial list is a list
    # containing two items/elements. Conventionally, we call them a and b separately. The initial list looks like this:
    # list = [a, b], where we can change the variable name into, say, "Fb_seq", which stands for "Fibonacci sequence".
    # Since there have been two items in the list, the first two indices (0 and 1) have been taken up by "a" and "b".
    # Therefore, the start of the range must be 2 because, as I said, 0 and 1 have been used to represent a and b.
    # Next, we should set the stop of the range. It depends on the number of the terms (including the first existing
    # two terms) the user wants.
    # For the sake of understanding directly, we call the variable for the number of terms "n".
    # Since the first two terms has been put there, we don't need to iterate through the indices of all the terms.
    # So, the stop should be n - 2. But the start has been set equal to 2, so (n - 2) has to be added another 2 to get
    # (n - 2) + 2 or shortly, n.
    # In a nutshell, the range which we iterate over should be range(2, n).
    Fb_seq.append(x)
print(f"The Fibonacci sequence with the first two terms {a} and {b} is: {Fb_seq}")




