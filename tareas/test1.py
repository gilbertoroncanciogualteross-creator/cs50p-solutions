# Exercise 1: Second Largest
# Print the second largest number in the list, without counting repeated numbers.

numbers = [4, 9, 2, 9, 7]
largest_num = 0
second_largest = 0

for x in numbers:
    if x > largest_num and second_largest != largest_num:
        largest_num += x
        second_largest += largest_num

print(second_largest);


# Your code here. It should print: 7
# When it works, also try [10, 3]. It should print: 3