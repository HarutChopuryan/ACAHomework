#### Homework 2 ####
def naturalNumberInput():
    while True:
        n = int(input("Input natural number: "))
        if n > 0:
            return n

#### Digit product ####
print(20*'-' + "Digit product" + 20*'-')
n = naturalNumberInput()
product = 1
while n != 0:
    digit = n % 10
    if digit != 0:
        product *= digit
    n //= 10
print("Product of nonzero digits: ", product)

#### Largest power of 3 ####
print(20*'-' + "Largest power of 3" + 20*'-')
def largestPowerOf3(n):
    i = 0
    largest_power_of_3 = 1
    while i < n:
        if 3**i <= n:
            largest_power_of_3 = i
        i += 1
    return 3**largest_power_of_3

N = naturalNumberInput()
print(f"Largest power of 3: {largestPowerOf3(N)}")

#### Triangle ####
print(20*'-' + "Triangle" + 20*'-')
def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        max_side = max(a, b, c)
        cos = 0
        if max_side == a:
            cos = (b**2 + c**2 - a**2) / (2*b*c)
        elif max_side == b:
            cos = (a**2 + c**2 - b**2) / (2*a*c)
        else:
            cos = (a**2 + b**2 - c**2) / (2*a*b)
        if cos == 0:
            print("Right triangle")
        elif cos < 0:
            print("Obtuse triangle")
        else:
            print("Acute triangle")
    else:
        print("No triangle")

a = naturalNumberInput()
b = naturalNumberInput()
c = naturalNumberInput()
print(isTriangle(a, b, c))

#### The root of the number ####
print(20*'-' + "The root of the number" + 20*'-')
def sumOFNumberDigits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

number = naturalNumberInput()
while True:
    sum_of_number_digits = sumOFNumberDigits(number)
    print(sum_of_number_digits)
    number = sum_of_number_digits
    if sum_of_number_digits < 10:
        break

#### Number of divisors ####
print(20*'-' + "Number of divisors" + 20*'-')
number = naturalNumberInput()
def divisorsCount(n):
    i = 1
    count = 0
    while i <= n:
        if n % i==0:
            count += 1
        i += 1
    return count

print(divisorsCount(number))

#### Quadratic equation ####
print(20*'-' + "Quadratic equation" + 20*'-')
a = float(input())
b = float(input())
c = float(input())
if a != 0:
    print("Quadratic equation")
    D = b**2 - 4*a*c
    if D < 0:
        print(f"Discriminant: {D}")
        print("No solutions")
    elif D == 0:
        print(f"Discriminant: {D}")
        print("One solution: ", -(b/(2*a)))
    else:
        x1 = (-b - D**0.5) / 2 * a
        x2 = (-b + D**0.5) / 2 * a
        print(f"Discriminant: {D}")
        print(f"Two solutions: {x1} {x2}")
elif b != 0:
    print("Non-quadratic equation")
    print(f"One solution: {-(c / b)}")
elif c != 0:
    print("Non-quadratic equation")
    print("No solutions")
else:
    print("Non-quadratic equation")
    print("Infinite solutions")