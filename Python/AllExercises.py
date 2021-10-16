from collections import Counter

def inputIntArray():
    list_size = int(input("Enter the list size (>0) "))
    print("Enter array elements")
    nums = []
    for _ in range(list_size):
        number = int(input())
        nums.append(number)
    return nums

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

#### Index sum ####

list_size = int(input("Enter the list size (>0) "))
print("Enter array elements")
a_array = []
for i in range(0, list_size):
    number = float(input())
    a_array.append(number)
indices_size = int(input("Enter the indices list size (>0) "))
indices = []
for i in range(0, indices_size):
    number = int(input())
    indices.append(number)

sum = 0
for i in indices:
    sum += a_array[i]
print(sum)

#### The most divisor-rich number ####

def divisorsCount(n):
    i = 1
    count = 0
    while i <= n:
        if n % i==0:
            count += 1
        i += 1
    return count

start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
numbers = []
numbers_divisors_count = []
for i in range(start_index, end_index + 1):
    numbers.append(i)
    numbers_divisors_count.append(divisorsCount(i))
index_of_max = numbers_divisors_count.index(max(numbers_divisors_count))
print(numbers[index_of_max])

# ### Lucky numbers ####

def numberToArrayOfDigits(num):
    digits = []
    while num != 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    return digits

even_pos_sum = 0
odd_pos_sum = 0
number = int(input("Enter number: "))
digits_array = numberToArrayOfDigits(number)
even_pos_sum = sum(digits_array[0 : len(digits_array) : 2])
odd_pos_sum = sum(digits_array[1 : len(digits_array) : 2])
if even_pos_sum == odd_pos_sum:
    print("Yes")
else:
    print("No")

# ### Monotonicity ####

def isIncreasing(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True

def isDecreasing(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] <= numbers[i+1]:
            return False
    return True

list_size = int(input("Enter number (>1): "))
print("Enter array elements")
numbers = []
for i in range(0, list_size):
    number = float(input())
    numbers.append(number)

if isIncreasing(numbers):
    print("Ascending")
elif isDecreasing(numbers):
    print("Descending")
else:
    print("Neither")

# ### Tree ####

bottom_star_number = int(input("Enter number of * in the bottom: "))
number_of_rows = (bottom_star_number // 2) + 1
for i in range(number_of_rows):
    for j in range(number_of_rows - i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()

#### Bayan ####

list_size = int(input("Enter the stores count (>0) "))
print("Enter stores names")
stores = []
for _ in range(list_size):
    store = input()
    stores.append(store)

count_of_stores = {}
set_of_stores = set(stores)
for key in set_of_stores:
    count_of_stores[key] = stores.count(key)
count_of_bayans = 0
for key, value in count_of_stores.items():
    if value != 1:
        count_of_bayans += value - 1
print(count_of_bayans)

#### Ice Cream Parlor ####

def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[icost] = i

money = int(input("Money: "))
cost = inputIntArray()
whatFlavors(cost, money)

#### Beautiful binary string ####

def beautifulBinaryString(str):
    count = 0
    for i in range(2,n):
        if str[i-2]=='0' and str[i-1]=='1' and str[i]=='0':
            str = str[:i] + '1' + str[i+1:]
            count += 1
    return count, str

n = int(input("Enter length of string: "))
binary_string = input("Enter binary string: ")
result = beautifulBinaryString(binary_string)
print(result[0])
print(result[1])

#### String power ####

def divideString(line, n):
    str_size = len(line)
    split_strings = []
    part_size = int(str_size/n)
    for index in range(0, len(line), part_size):
        split_strings.append(line[index : index + part_size])
    return split_strings

line = input("Enter string: ")
power = int(input("Enter string power: "))
split_string = []
if power > 0:
    print(line * power)
elif power < 0:
    if power == -1:
        print(line)
    else:
        substrings = divideString(line, -power)
        is_rootable = True
        for i in range(len(substrings)-1):
            if substrings[i] != substrings[i+1]:
                is_rootable = False
        if is_rootable:
            print(substrings[0])
        else:
            print("Undefined")
else:
    print("")

#### Super reduced string ####

def superReducedString(s):
    stack = []
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack)

s = input()
print(superReducedString(s))

#### Strong password ####

def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    count = 0    
    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in special_characters for i in password) == False:
        count+=1
    return max(count,6-n)

n = int(input())
password = input()
answer = minimumNumber(n, password)
print(answer)

#### Two strings ####

def twoStrings(str1, str2):
    m1 = set(str1)
    m2 = set(str2)
    if set.intersection(m1,m2):
        return "Yes"
    return "No"

string_count = int(input())
for i in range(string_count):
    str1 = input()
    str2 = input()
    result = twoStrings(str1, str2)
    print(result)

#### Jewels and stones ####

class JewelsAndStones:

    def __init__(self, jewels, stones):
        self.jewels = jewels
        self.stones = stones
        self.jewels_array = list(jewels)
    
    def output(self):
        count = 0
        for ch in self.stones:
            count += self.jewels_array.count(ch)
        return count

jewels = input("Input jewels: ")
stones = input("Input stones: ")
jewels_and_stones = JewelsAndStones(jewels, stones)
out = jewels_and_stones.output()
print(out)

#### Number of good pairs ####

class NumberOfGoodPairs:

    def __init__(self, nums):
        self.nums = nums[:]
        self.good_pairs = []
    
    def constructGoodPairs(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if self.nums[i] == self.nums[j] and i < j:
                    if self.good_pairs.count([i, j]) != 0:
                        continue
                    else:
                        self.good_pairs.append([i, j])
        return self.good_pairs, len(self.good_pairs)

list_size = int(input("Enter the list size (>0) "))
print("Enter array elements")
nums = []
for _ in range(list_size):
    number = int(input())
    nums.append(number)

num_of_good_pairs = NumberOfGoodPairs(nums)
good_pairs = num_of_good_pairs.constructGoodPairs()
print(good_pairs[1])
print(good_pairs[0])

#### Unique number of occurences ####

class UniqueOccurences:

    def __init__(self, arr):
        self.arr = arr[:]
        self.arr_unique_elements = set(arr)
        self.count_of_occurences = []
    
    def isUnique(self):
        for elem in self.arr_unique_elements:
            count = self.arr.count(elem)
            self.count_of_occurences.append(count)
        for i in range(len(self.count_of_occurences) - 1):
            if self.count_of_occurences[i] == self.count_of_occurences[i+1]:
                return False
        return True

list_size = int(input("Enter the list size (>0) "))
print("Enter array elements")
nums = []
for _ in range(list_size):
    number = int(input())
    nums.append(number)

unique_occ = UniqueOccurences(nums)
print(unique_occ.isUnique())

#### Distribute candies ####

class Candy:

    def __init__(self, candies):
        self.candy_type = candies[:]
        self.different_types = set(candies)

    def maxTypes(self):
        if len(self.candy_type) / 2 < len(self.different_types):
            return len(self.candy_type) / 2
        else:
            return len(self.different_types)

candy_type = inputIntArray()
candy = Candy(candy_type)
print(candy.maxTypes())

#### Making anagrams ####

def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    difference_a = count_a - count_b
    difference_b = count_b - count_a
    result = sum(difference_a.values()) + sum(difference_b.values())
    return result

a = input()
b = input()
result = makeAnagram(a, b)
print(result)

#### Find Words That Can Be Formed by Characters ####

class GoodWords:

    def __init__(self, words, chars):
        self.words = words[:]
        self.chars = chars[:]
        self.good_words = []

    def lengthsOfGoodWords(self):
        flag = False
        length = 0
        for word in self.words: 
            for char in word:
                if word.count(char) <= self.chars.count(char):
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                length += len(word)
        return length

list_size = int(input("Enter the list size (>0) "))
print("Enter array elements")
words = []
for _ in range(list_size):
    word = input()
    words.append(word)

chars = input("Chars: ")
good_words = GoodWords(words, chars)
length = good_words.lengthsOfGoodWords()
print(length)