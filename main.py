def sumOfDigits(num):
    result = 0
    while num > 0:
        rem = num % 10
        result = result + rem
        num = num // 10
    return result


def countDigits(num):
    count = 0
    while num > 0:
        rem = num % 10
        count += 1
        num = num // 10
    return count

def reverseDigits(num):
    result = 0
    while num > 0:
        rem  = num % 10
        result = result * 10 + rem
        num = num // 10
    return result

def isPalindrome(num):
    cpy = num
    op = reverseDigits(num)
    if op == cpy:
        return True
    return False

nums = 12321
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(nums))
print(reverseDigits(nums))
print(countDigits(nums))
print(sumOfDigits(nums))
