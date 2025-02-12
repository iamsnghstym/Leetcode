def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x > 9 and x % 10 == 0):
        return False

    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10

    return True if x == rev or x == rev // 10 else False