# Program to create a list of the Fibonacci-like sequence whose first two terms are obtained from user input and can be
# any two random integers, and then to find out the smallest value of n for which the sums of the first n and n + 1
# terms are both exactly divided by some number, which is also obtained from the user input (say, 11).

a = int(input("Enter the first term: "))
b = int(input("Enter the second term: "))
Fb_seq = [a, b]
n = int(input("Enter the number of terms: "))
for i in range(2, n):
    x = Fb_seq[i-1] + Fb_seq[i-2]
    Fb_seq.append(x)
print(f"\nThe Fibonacci sequence with the first two terms {a} and {b} is: {Fb_seq}")

Sum = 0
d = int(input("\nEnter the divisor: "))
for x in Fb_seq:
    Sum += x
    if Sum != 0:
        if Sum % d == 0 and (Sum + Fb_seq[(Fb_seq.index(x) + 1)]) % d == 0:
            break
print(f"\nThe partial sums of the first {Fb_seq.index(x)} and {Fb_seq.index(x) + 1} terms of the Fibonacci "
      f"sequence are both divisible by {d}, if the first two terms are 1 and 1, rather than 0 and 1. "
      f"\nThe partial sums of the first {Fb_seq.index(x) + 1} and {Fb_seq.index(x) + 2} terms of the Fibonacci "
      f"sequence are both divisible by {d}, if the first two terms are 0 and 1, rather than 1 and 1.")
print(f"\nIn detail, the partial sum of the first {Fb_seq.index(x)} (or {Fb_seq.index(x) + 1}) terms is {Sum}, "
      f"which is equal to {Sum / d} if exactly divided by {d}.\n"
      f"The partial sum of the first {Fb_seq.index(x) + 1} (or {Fb_seq.index(x) + 2}) terms is"
      f" {Sum + Fb_seq[Fb_seq.index(x) + 1]}, "
      f"which is equal to {(Sum + Fb_seq[Fb_seq.index(x) + 1]) / d} if exactly divided by {d}.")
