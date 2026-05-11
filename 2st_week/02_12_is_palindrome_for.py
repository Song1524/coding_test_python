input = "abcba"


def is_palindrome(string):

    # n = len(string) - 1
    #
    # for char in string:
    #     if char != string[n]:
    #         return False
    #
    #     n -= 1

    n = len(string)

    for i in range(n // 2):
        if string[i] != string[n - 1 - i]:
            return False

    return True


print(is_palindrome(input))