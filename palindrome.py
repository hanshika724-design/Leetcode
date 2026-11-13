
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            last = x % 10
            rev = rev * 10 + last
            x = x // 10

        return x == rev or x == rev // 10


# Main program for VS Code
x = int(input("Enter a number: "))

obj = Solution()

if obj.isPalindrome(x):
    print("Palindrome")
else:
    print("Not Palindrome")
