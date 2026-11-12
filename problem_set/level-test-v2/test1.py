# Given a list of numbers, print the second largest, not counting duplicates.

numbers = [4, 9, 2, 9, 7]
# should print: 7
# also test [10, 3] -> 3

numbers = set([4, 9, 2, 9, 7])
numbers = sorted(numbers)

if len(numbers) > 1:
    print(numbers[-2])
else:
    print(None)