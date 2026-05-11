input = "abcba"


def is_palindrome(string):
    n = len(string)

    if n <= 1:
        return True

    if string[0] != string[n - 1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))