def diff_palindrome(number):
    palindrome = int(str(number)[::-1])
    return abs(number - palindrome)

print(diff_palindrome(int(input())))