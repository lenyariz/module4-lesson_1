def check_palindrome(string: str) -> bool:
    if string == string[::-1]:
        return True
    else:
        return False
