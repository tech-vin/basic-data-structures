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

def reverseWithXSpace(num):
    # same as reverseDigits(), hence skipping
    pass

def largest_Digit(num):
    result = 0
    while num > 0:
        rem = rem % 10
        if rem > result:
            result = rem
        num = num // 10
    return result

def productOfDigits(num):
    result = 1
    while num > 0:
        rem = num % 10
        result = result * rem
        num = num // 10
    return result

def powerOf2(num):
    return num > 0 and (num & (num-1)) == 0

def countEvenOddDigits(num):
    even, odd = 0, 0
    while num > 0:
        rem  = num % 10
        if rem % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    return f"Even Count: {even} Odd count: {odd} "

def firstAndLastDigit(num):
    last_digit = num % 10
    while num >= 10:
        num = num // 10
    first_digit = num
    return f"fist digit: {first_digit} last digit: {last_digit}"

def isArmstrongNumber(num):
    cpy = num
    power = countDigits(num)
    result = 0
    while num > 0:
        rem  = num % 10
        result = result + (rem ** power)
        num = num // 10
    if result == cpy:
        return f"{cpy} is an armstrong number."
    else:
        return f"{cpy} is not an armstrong number."

nums = 12321
print(isArmstrongNumber(nums))
print(isArmstrongNumber(153))
print(isArmstrongNumber(2497))
print(firstAndLastDigit(nums))
print(firstAndLastDigit(12345))
print(countEvenOddDigits(nums))
print(countEvenOddDigits(1234))
print(powerOf2(nums))
print(powerOf2(16))
print(productOfDigits(nums)) # 12
print(isPalindrome(123))
print(isPalindrome(121))
print(isPalindrome(nums))
print(reverseDigits(nums))
print(countDigits(nums))
print(sumOfDigits(nums))
