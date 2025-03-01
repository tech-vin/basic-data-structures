def sumOfDigits(num):
    result = 0
    while num > 0:
        rem = num % 10
        result = result * 10 + rem
        num = num // 10
    return result

print(sumOfDigits(12312))