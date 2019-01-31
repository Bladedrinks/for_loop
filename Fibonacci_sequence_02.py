# Program to work out the sum of the first n terms in the Fibonacci sequence.

# The Fibonacci sequence is:
Fb_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
          46368, 75025, 121393, 196418, 317811, 514229]

# Initialize the variable for summation.
Sum = 0

# To work out the summation of the first n terms, practically we need to add each term to the initial "sum" one by one.
# After adding up all the first n terms, we're gonna be getting the sum of them. Each term added to the "sum" variable
# can be called "counter" (literally meaning a stuff that is used for counting).
# We create a variable called "x" for counter over here.
for x in Fb_seq:
    Sum += x
    if Sum != 0:
        if Sum % 11 == 0 and (Sum + Fb_seq[(Fb_seq.index(x) + 1)]) % 11 == 0:
            break
print(f"\nThe partial sums of the first {Fb_seq.index(x)} and {Fb_seq.index(x) + 1} terms of the Fibonacci "
      f"sequence are both divisible by 11, if the first two terms are 1 and 1, rather than 0 and 1. "
      f"\nThe partial sums of the first {Fb_seq.index(x) + 1} and {Fb_seq.index(x) + 2} terms of the Fibonacci "
      f"sequence are both divisible by 11, if the first two terms are 0 and 1, rather than 1 and 1.")
print(f"\nIn detail, the partial sum of the first {Fb_seq.index(x)} (or {Fb_seq.index(x) + 1}) terms is {Sum}, "
      f"which is equal to {Sum / 11} if exactly divided by 11.\n"
      f"The partial sum of the first {Fb_seq.index(x) + 1} (or {Fb_seq.index(x) + 2}) terms is"
      f" {Sum + Fb_seq[Fb_seq.index(x) + 1]}, "
      f"which is equal to {(Sum + Fb_seq[Fb_seq.index(x) + 1]) / 11} if exactly divided by 11.")
