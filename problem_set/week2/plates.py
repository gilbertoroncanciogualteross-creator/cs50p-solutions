# Implement a program that prompts the user for a vanity plate and then output Valid if meets
# all of the requirements or Invalid if it does not. Assume that any letters in the user's input
# will be upercase.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def only_letters_and_numbers(s):
    return s.isalnum()

def start_with_two_letters(s):
    return s[0].isalpha() and s[1].isalpha()

def maximum_and_minimum_characters(s):
    return 2<=len(s)<=6

def numbers_not_in_middle(s):
    exist_a_num = False
    for i in s:
        if i.isdigit():
            if i == "0" and not exist_a_num:
                return False
            exist_a_num = True
        if not i.isdigit() and exist_a_num:
            return False

    return True

def is_valid(s):
    if not only_letters_and_numbers(s):
        return False

    if not maximum_and_minimum_characters(s):
        return False

    if not start_with_two_letters(s):
        return False

    if not numbers_not_in_middle(s):
        return False

    return True
    
main()