
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        while x != 0:
            last = x % 10
            x = int(x / 10)

            if rev > 2147483647 // 10 or (rev == 2147483647 // 10 and last > 7):
                return 0

            if rev < -2147483648 // 10 or (rev == -2147483648 // 10 and last < -8):
                return 0

            rev = rev * 10 + last

        return rev


x = int(input("Enter a number: "))
obj = Solution()
print(obj.reverse(x))
