"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Please enter a non-zero denominator: "))

    while denominator == 0:
        denominator = int(input("The denominator entered was zero. Please enter a non-zero denominator: "))

    fraction = numerator / denominator

    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1) A ValueError will occur if something that is not an integer is entered. i.e. - a letter, or a decimal number.
#    Negative numbers are accepted.
# 2) A ZeroDivisionError will occur whenever zero is entered as a denominator.
# 3) A non-technical way to "avoid a ZeroDivisionError is to simply tell the user in the denominator input line
#    to not enter zero. Or, before the fraction is processed, a while statement could be used to see if a zero was
#    entered, and if so, ask the user to enter a different number that isn't zero, before calculating the fraction.
