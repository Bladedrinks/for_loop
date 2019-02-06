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
    ord_num = str(len(nums) + 1)    # Each number/term in the list has an ordinal number, like the Hindu-Arabic numerals
    # as in 1st, 2nd, 3rd, 4th, ..., 10th, 11th, 12th, 13th, 14th, ..., 20th, 21st, 22nd, 23rd, 24th, ..., 100th, 101st,
    # 102nd, 103rd, 104th, etc. Usually, each number's ordinal number has the same value as the length of the list which
    # can be seen as starting from the first item/element up to it. Let's say, we've got a list like this:
    #
    #                                       ls = [600, 470, 600, 170, 430, 300]
    #                                    index : 0    1    2    3    4    5
    #                              ordinal num :  1st  2nd  3rd  4th  5th  6th
    #
    # where the number 170 is the 4th number/item/element in the list. If we suppose that the list is stopped just at
    # this number, then the length of this list (i.e. the value of the len() function) must be 4 (because the list
    # contains four items in it). It is obvious to find that the ordinal number of 170 and the length of the list which
    # is seen as being stopped at 170 have the same value, which is 4. While coding, we can write their relationship
    # like this:
    #
    #                                     ord_num = len(ls[:(ls.index(170) + 1)])
    #
    # The code shown above is the same as:
    #
    #                                     ord_num = len(ls[:4])
    #
    # where ls[:-4] returns [600, 470, 600, 170] whose length is 4. So, ord_num = 4, which is true because 170 is the
    # 4th number in the list.
    # The method for working out the ordinal number/position of some number in a list isn't flawless especially when
    # there are like numbers (i.e. numbers that have the same value) like, in the above example, the 1st number of 600
    # and the 3rd number of 600. Every time when you use the list.index() method on a number of 600, the code -
    # ls.index(600) - will return 0, rather than 2. This is what the syntax of list.index() method regulates.

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
print(f'''
 -----------------------
   The list of numbers  :  {nums}
 -----------------------
''')
nums.sort()  # Sort the numbers in the given list in a specific order (by default, in an ascending order).
print(f'''
 ---------------------------------------------
   The list of numbers in an ascending order  :  {nums}
 ---------------------------------------------
''')


# # Below is another version/solution of the 1st part of the program, which doesn't need to initialize the variable
# # standing for the first term. We can put the assignment of the first term inside the while loop.
#
# n = int(input("\nEnter the number of terms: "))
# nums = []
# while len(nums) <= (n - 1):  # Say, n = 3, meaning the list contains 3 numbers. So, the right side of the <= comparison
#     # operation will be 2. len(nums) <= 2, as the test expression of a while loop, can give us three chances to enter
#     # the body of the loop because the initial value of len(nums) is 0 and numbers that are less than or equal to 2
#     # have three: 0, 1 and 2.
#     ord_num = str(len(nums) + 1)  # Still using the above example, the ordinal number generally starts at 1 (first).
#     # That's why we have to add 1 to len(nums). When len(nums) = 0, ord_num = 0 + 1 = 1. When len(nums) = 1, ord_num =
#     # 1 + 1 = 2. When len(nums) = 2, ord_num = 2 + 1 = 3. While string formatting the variable ord_num, these three
#     # ordinal numbers changes into 1st, 2nd and 3rd.
#     if ord_num[-2:] == str(11) or ord_num[-2:] == str(12) or ord_num[-2:] == str(13):
#         x = float(input(f"\nEnter the {ord_num}th number: "))
#         nums.append(x)
#     elif ord_num[-1] == str(1) or ord_num[-1] == str(2) or ord_num[-1] == str(3):
#         if ord_num[-1] == str(1):
#             x = float(input(f"\nEnter the {ord_num}st number: "))
#             nums.append(x)
#         elif ord_num[-1] == str(2):
#             x = float(input(f"\nEnter the {ord_num}nd number: "))
#             nums.append(x)
#         else:
#             x = float(input(f"\nEnter the {ord_num}rd number: "))
#             nums.append(x)
#     else:
#         x = float(input(f"\nEnter the {ord_num}th number: "))
#         nums.append(x)
# print(f'''
#  -----------------------
#    The list of numbers  :  {nums}
#  -----------------------
# ''')


# The 2nd part of the program which is to work out the arithmetic mean of the numbers which we get from the 1st part.
# Initialize the summation of the list of numbers.
Sum = 0
for x in nums:
    Sum += x
print(f'''
 ----------------------
   The sum of numbers  :  {Sum}
 ----------------------
''')
# Work out the (arithmetic) mean.
m = Sum / n
print(f'''
 ---------------------------
   The mean of numbers (μ)  :  {m}
 ---------------------------
''')


# The 3rd part of the program which is to get the variance.
# Initialize the variance which is named based off of the mathematical symbol of the standard deviation,
# which is the Greek letter σ (pronounced /sigma/). The variance is written as σ^2 (meaning σ squared or σ raised up to
# the 2nd power).
σ2 = 0
for x in nums:
    σ2 += ((x - m) ** 2) / n
    #                      (X1 - mean)^2 + (X2 - mean)^2 + (X3 - mean)^2 + ... + (Xn - mean)^2
    #          Variance = ---------------------------------------------------------------------
    #                                                      n
print(f'''
 ----------------------
      The variance     :  {round(σ2, 10)}
 ----------------------
''')


# The 4th part of the program which is to yield the standard deviation.
σ = sqrt(σ2)
print(f'''
 ----------------------------
  The Standard Deviation (σ) :  {round(σ, 7)} (to 7 decimal places) or {round(σ)} (to the nearest one)
 ----------------------------
   +1 Standard Deviation     :  From {m} To {round(m + σ)} 
 ----------------------------
   -1 Standard Deviation     :  From {round(m - σ)} To {m} 
 ----------------------------
''')


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
 -------------------------------   
   The normal number list       :  {nm_nums}

   The extra-big number list    :  {xb_nums}

   The extra-small number list  :  {xs_nums}
 -------------------------------
''')

print('''
 -------------------------------
      Detailed Explanation      :
 -------------------------------\
''')
ls = [nm_nums, xb_nums, xs_nums]
for X_nums in ls:
    if len(X_nums) == 1:
        if X_nums == nm_nums:
            print(f"\n   {nm_nums[0]} is the only number that is within one Standard Deviation. "
                  f"It is the only normal number.")
        elif X_nums == xb_nums:
            print(f"\n   {xb_nums[0]} is the only number that is greater than one Standard Deviation. "
                  f"It is the only number that is extra big.")
        else:  # X_nums == xs_nums
            print(f"\n   {xs_nums[0]} is the only number that is smaller than one Standard Deviation. "
                  f"It is the only number that is extra small.")
    else:  # len(X_nums) > 1:
        if X_nums == nm_nums:
            nm_nums_str = ""
            for i in range(len(nm_nums)):
                if i == len(nm_nums) - 2:  # The index of the penultimate number in the list nm_nums. (Notice that the
                    # index of the last number in the list is: len(nm_nums) - 1
                    nm_nums_str += f"{nm_nums[i]} and "
                else:  # i != len(nm_nums) - 2:
                    nm_nums_str += f"{nm_nums[i]}, "
            nm_nums_str = nm_nums_str[:-2]  # Unlike list which is mutable (by using the [] index operator,
            # the : slicing operator and the = assignment operator on the target item or range of items),
            # string is immutable, meaning that elements of a string can not be changed once the string value has been
            # assigned to the variable. But you can reassign a different new string to the same variable if you really
            # want to change an item or a range of items.
            print(f"\n   Numbers that are within one Standard Deviation are: {nm_nums_str}, which are normal.")
        elif X_nums == xb_nums:
            xb_nums_str = ""
            for i in range(len(xb_nums)):
                if i == len(xb_nums) - 2:
                    xb_nums_str += f"{xb_nums[i]} and "
                else:  # i != len(xb_nums) - 2:
                    xb_nums_str += f"{xb_nums[i]}, "
            xb_nums_str = xb_nums_str[:-2]
            print(f"\n   Numbers that are greater than one Standard Deviation are: {xb_nums_str}, which are extra big.")
        else:  # X_nums == xs_nums
            xs_nums_str = ""
            for i in range(len(xs_nums)):
                if i == len(xs_nums) - 2:
                    xs_nums_str += f"{xs_nums[i]} and "
                else:  # i != len(xb_nums) - 2:
                    xs_nums_str += f"{xs_nums[i]}, "
            xs_nums_str = xs_nums_str[:-2]  # The right side of the = assignment operator is designed to get rid of the
            # trailing comma and whitespace character.
            print(f"\n   Numbers that are smaller than one Standard Deviation are: {xs_nums_str}, which are extra small.")


# # Below is another version/solution of the 5th part of the program, which has refactored the original if...else...
# # conditional structure.
# nm_nums = []
# xb_nums = []
# xs_nums = []
# for x in nums:
#     if abs(x - m) <= σ:
#         nm_nums.append(x)
#     elif x - m > σ:
#         xb_nums.append(x)
#     elif x - m < -σ:
#         xs_nums.append(x)
# print(f'''
#  -------------------------------
#    The normal number list       :  {nm_nums}
#
#    The extra-big number list    :  {xb_nums}
#
#    The extra-small number list  :  {xs_nums}
#  -------------------------------
# ''')
#
# print('''
#  -------------------------------
#       Detailed Explanation      :
#  -------------------------------\
# ''')
# if len(nm_nums) == 1:
#     print(f"\n   {nm_nums[0]} is the only number that is within one Standard Deviation. "
#           f"It is the only normal number.")
# elif len(nm_nums) > 1:
#     print(f"\n   Numbers that are within one Standard Deviation are: {nm_nums}, which are normal.")
# if len(xb_nums) == 1:
#     print(f"\n   {xb_nums[0]} is the only number that is greater than one Standard Deviation. "
#           f"It is the only number that is extra big.")
# elif len(xb_nums) > 1:
#     print(f"\n   Numbers that are greater than one Standard Deviation are: {xb_nums}, which are extra big.")
# if len(xs_nums) == 1:
#     print(f"\n   {xs_nums[0]} is the only number that is smaller than one Standard Deviation. "
#           f"It is the only number that is extra small.")
# elif len(xs_nums) > 1:
#     print(f"\n   Numbers that are smaller than one Standard Deviation are: {xs_nums}, which are extra small.")





