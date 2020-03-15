import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Line 1 resulted in 15.
# The smallest number that could have been generated in Line 1 was 5, and the largest was 20.
# Line 2 printed the number 9.
# The smallest number that could have been generated in Line 2 was a 3, and the largest being 9.
# Line 2 could not have produced a 4, as the code has a step of 2, starting from 3. 4 is only one step from 3, not 2.
# Line 3 produced the float number 3.336785581965838.
# The smallest number that could have been generated in Line 3 was 2.5, and the largest was 5.5, depending on rounding.

print(random.randint(1, 100))
