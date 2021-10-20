#### The Goldbach Conjecture ####

primes = []
def goldbachFunction(num):
    is_prime = False
    if num > 1:
        if num == 2:
            is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True

    if is_prime:
        return
    else:
        if (num <= 2 or num % 2 != 0):
            print("Invalid Input")
            return
        else:
            for i in range(2, num + 1):
                for j in range(2,i):
                    if i % j == 0:
                        break
                else:
                    primes.append(i)
        i = 0
        while (primes[i] <= num // 2):
            diff = num - primes[i]
            if diff in primes:
                print(primes[i], " ", diff)
                return
            i += 1

number = int(input("Input number (<10000): "))
print(goldbachFunction(number))

#### Palindrome numbers ####

def isPalindrome(number):
    temp = number
    rev = 0
    while number > 0:
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if temp == rev:
        return True
    else:
        return False

startIndex = int(input("Enter a number: "))
endIndex = int(input("Enter a number: "))
for i in range(startIndex, endIndex + 1):
    if isPalindrome(i):
        print(i)

#### Suffix sums ####

list_size = int(input("Enter the list size "))
print("Enter array elements")
a_array = []
b_array = []
for _ in range(list_size):
    number = float(input())
    a_array.append(number)
for i in range(len(a_array)):
    sum = 0
    for j in range(len(a_array) - 1, i - 1, -1):
        sum += a_array[j]
    b_array.append(sum)
print(b_array)

#### Cyclic shift ####

list_size = int(input("Enter the list size "))
number_of_times = int(input("Enter number of times: "))
print("Enter array elements")
a_array = []
for i in range(0, list_size):
    number = float(input())
    a_array.append(number)

temp = number_of_times % list_size
if temp == 0:
    number_of_moves = list_size - number_of_times
else:
    number_of_moves = list_size - temp
for i in range(0, number_of_moves):
    a_array = a_array[1::] + a_array[:1:]
print(a_array)

# ### Tree ####

bottom_star_number = int(input("Enter number of * in the bottom: "))
number_of_rows = (bottom_star_number // 2) + 1
for i in range(number_of_rows):
    for j in range(number_of_rows - i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()