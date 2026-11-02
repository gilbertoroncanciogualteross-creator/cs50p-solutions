# Exercise 3: Palindrome
# A phrase is a palindrome if it reads the same forwards and backwards,
# ignoring spaces and uppercase letters.

def is_palindrome(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")

    for x in phrase:
        for y in reversed(phrase):
            if x == y:
                return "true"

print(is_palindrome("Never odd or even"))