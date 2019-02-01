# Program to work out the variation and standard deviation of a list of numbers and finally to check which number is
# within one Standard Deviation (in order to find out which number is normal, which is extra big or extra small).

from math import *
# The 1st part of the program which is to ask the user for their desired list of numbers.
# Initialized the number of terms, the list of numbers and the first number/term of the list.
n = int(input("\nEnter the number of terms: "))
nums = []
x = float(input("\nEnter the 1st number: "))
nums.append(x)
# Since the original value of len(nums) is already 1, the right-hand side of the <= comparison operator must be set
# equal to n - 1 . If we set the right side equal to n (say, n = 3), then the while test expression will be: 1 <= 3 .
# In while loop, the test expression is checked first. If the test expression evaluates to True, the body of loop is
# executed. After one try, the test expression will be checked again. The process (iteration) continues until the test
# expression evaluates to False. The rule applies to this example case as well:
# In this case, the test expression is: len(nums) <= (n - 1)
# When the while loop does its first check, the test expression is 1 <= 3 (if we set the right side equal to n, which is
# 3). 1 is less than or equal to 3, so the test expression evaluated to True and then the body of loop is allowed to be
# executed. The result of the first try is: len(nums) == 2 . 2 is less than 3, so we can do a second try. The result of
# the second try is: len(nums) == 3. 3 is equal to 3, so we can do a third try.
# The result of the third try is: len(nums) == 4, which means the list of numbers has 4 terms in it. That's not what we
# want. Therefore, we need to modify the test expression either by setting the right side equal to (n - 1) or by
# changing the <= operator into the < operator.
# Notice that what determines whether a while loop continues or not is the boolean value of the test expression, rather
# than other factors or conditions. In programming, intuition is important, but is also an obstacle, sometimes.
# Remember: Think on keyboard. Don't think in mind.
while len(nums) <= (n - 1):
    ord_num = str(len(nums) + 1)
    if ord_num[-2:] == str(11) or ord_num[-2:] == str(12) or ord_num[-2:] == str(13):
        x = float(input(f"\nEnter the {ord_num}th number: "))
        nums.append(x)
    elif ord_num[-1] == str(1) or ord_num[-1] == str(2) or ord_num[-1] == str(3):
        if ord_num[-1] == str(1):
            x = float(input(f"\nEnter the {ord_num}st number: "))
            nums.append(x)
        elif ord_num[-1] == str(2):
            x = float(input(f"\nEnter the {ord_num}nd number: "))
            nums.append(x)
        else:
            x = float(input(f"\nEnter the {ord_num}rd number: "))
            nums.append(x)
    else:
        x = float(input(f"\nEnter the {ord_num}th number: "))
        nums.append(x)
print(f"\nThe list of numbers is: {nums}")

# The 2nd part of the program which is to work out the arithmetic mean of the numbers which we get from the 1st part.
# Initialize the summation of the list of numbers.
Sum = 0
for x in nums:
    Sum += x
print(f"\nThe summation of the list of numbers is: {Sum}")
# Work out the (arithmetic) mean.
m = Sum / n
print(f"\nThe arithmetic mean of these numbers is: {Sum / n}")


# The 3rd part of the program which is to get the variance.
# Initialize the variance which is named based off of the mathematical symbol of the standard deviation,
# which is the Greek letter σ (pronounced /sigma/). The variance is written as σ^2 (meaning σ squared or σ raised up to
# the 2nd power).
σ2 = 0
for x in nums:
    σ2 += ((x - m) ** 2) / n
    #              (X1 - mean) ** 2 + (X2 - mean) ** 2 + (X3 - mean) ** 2 + ... + (Xn - mean) ** 2
    # Variance == ---------------------------------------------------------------------------------
    #                                                  n
print(f"\nThe Variance is: {round(σ2, 10)}")

# The 4th part of the program which is to yield the standard deviation.
σ = sqrt(σ2)
print(f"\nThe Standard Deviation is approximately equal to: {round(σ, 7)} (to 7 decimal places) "
      f"or {round(σ)} (to the nearest one).")

# The 5th part of the program which is to find out which number is within one Standard Deviation. And then we can know
# that which number is normal, which is extra big or extra small.
nm_nums = []
xb_nums = []
xs_nums = []
for x in nums:
    if abs(x - m) <= σ:
        nm_nums.append(x)
    elif x - m > σ:
        xb_nums.append(x)
    elif x - m < -σ:
        xs_nums.append(x)
print(f'''
The normal number list: {nm_nums}
The extra-big number list: {xb_nums}
The extra-small number list: {xs_nums}
''')
ls = [nm_nums, xb_nums, xs_nums]
for X_nums in ls:
    if len(X_nums) == 1:
        if X_nums == nm_nums:
            print(f"{nm_nums[0]} is the only number that is within one Standard Deviation. "
                  f"It is the only normal number.")
        elif X_nums == xb_nums:
            print(f"{xb_nums[0]} is the only number that is greater than one Standard Deviation. "
                  f"It is the only number that is extra big.")
        else:  # X_nums == xs_nums
            print(f"{xs_nums[0]} is the only number that is smaller than one Standard Deviation. "
                  f"It is the only number that is extra small.")
    else:
        if X_nums == nm_nums:
            print(f"Numbers that are within one Standard Deviation are: {nm_nums}, which are normal.")
        elif X_nums == xb_nums:
            print(f"Numbers that are greater than one Standard Deviation are: {xb_nums}, which are extra big.")
        else:  # X_nums == xs_nums
            print(f"Numbers that are smaller than one Standard Deviation are: {xs_nums}, which are extra small.")






