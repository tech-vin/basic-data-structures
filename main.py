def sumOfDigits(num):
    result = 0
    while num > 0:
        rem = num % 10
        result = result * 10 + rem
        num = num // 10
    return result


def countDigits(num):
    count = 0
    while num > 0:
        rem = num % 10
        count += 1
        num = num // 10
    return count

nums = 12321
print(countDigits(nums))
print(sumOfDigits(nums))