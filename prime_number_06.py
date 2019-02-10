# Program to find and display all PRIME factors of a number (mainly a composite number).


# Define a function to insert a conjunction of " and " into string.
def insert_and_in(list_name):
    """
    Insert the conjunction of " and " into a string (usually between the penultimate word and the last word.
    For example, we got a list:

                                          factors = [1, 3, 7, 21].

    We want to change it into a string without square brackets outside, like this:

                                                1, 3, 7 and 21

    We can pass in the list name "factors" as the parameter by assigning the variable "factors" to the variable
    "list_name" and we will get a list shown above."""
    list_in_str = ""
    # test case: list_name = [45, 98, 45]
    # index:                  -3  -2  -1
    # test case: list_name = [45]
    # index:                  -1
    for i in range(-len(list_name), 0):
        if i == -1:
            list_in_str += f"{list_name[i]}"
        elif i == -2:
            list_in_str += f"{list_name[i]} and "
        else:
            list_in_str += f"{list_name[i]}, "
    return list_in_str
# End of the Function Definition.


# Define a function for checking if a number is prime or not before calling it later.
def prime_check(num):
    """Check if a number is prime or not and display it if it is prime."""
    if num > 1:
        for i in range(2, num):
            if num % i == 0:  # if num can be exactly divided by i, then ...
                # print(f"{num} is not prime, since {i} times {num // i} equals {num}.")
                break
        else:
            return num
# End of the Function Definition.


# Define a function for checking if a number is composite or not before calling it later.
def composite_check(num):
    """Check if a number is composite or not and display it if it is composite."""
    if num > 3:
        # Definition of "composite number":
        # Any natural number greater than 1 that is not prime is a composite number.
        for i in range(2, num):
            if num % i == 0:  # if num can be exactly divided by i, then ...
                # print(f"{num} is not prime, since {i} times {num // i} equals {num}.")
                return num
# End of the Function Definition.


# Define a function for finding out and displaying all factors of the input number, prime and/or composite, except 1 and
# itself.
def factors_of_(num):
    """Find out and display all factors of the input number, prime and/or composite, not including 1 and itself."""
    # Initialize the list "factors" with an empty list.
    factors = []
    for d in range(2, num):
        if num % d == 0:
            factors.append(d)
    if factors:
        return factors
    else:
        print(f"{num} has only two factors: 1 and {num}, since {num} is a prime number.")
# End of the definition of the user-defined function.


# Define a function for checking if each one of factors of the given number is prime or not and display it together
# with other prime factors, if any, in list form.
def prime_factors(factors):
    """
    Distinguish prime factors from the given list of all factors of a number.
    The parameter must be a list.
    """
    prim_factors = []
    for factor in factors:
        if prime_check(factor):
            prim_factors.append(prime_check(factor))
    return prim_factors
# End of the user-defined function.


# Define a function for checking if each one of factors of the given number is composite or not and display it together
# with other composite factors, if any, in list form.
def composite_factors(factors):
    """
    Only take composite factors from the given list of all factors of a number.
    The parameter must be a list.
    """
    comp_factors = []
    for factor in factors:
        if composite_check(factor):
            comp_factors.append(composite_check(factor))
    return comp_factors
# End of the user-defined function.


# Program to find out and display all factors of the input number, prime and/or composite.
num = int(input("Enter your number: "))
print(f"\nFactors of {num} (not including 1 and itself) are: ")
print(factors_of_(num))
if factors_of_(num):
    print(f"\nPrime factors of {num} (not including itself) are: ")
    print(prime_factors(factors_of_(num)))
if factors_of_(num):
    print(f"\nComposite factors of {num} (not including itself) are: ")
    print(composite_factors(factors_of_(num)))











