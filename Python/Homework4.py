def inputMatrix():
    row_count = int(input("Enter the row count: "))
    column_count = int(input("Enter the column count: "))
    print("Enter matrix elements")
    matrix = []
    for r in range(row_count):
        row = []
        for c in range(column_count):
            number = int(input())
            row.append(number)
        matrix.append(row)
    return matrix

def inputIntArray():
    list_size = int(input("Enter the list size (>0) "))
    print("Enter array elements")
    nums = []
    for _ in range(list_size):
        number = int(input())
        nums.append(number)
    return nums

def inputStrArray():
    list_size = int(input("Enter the array size (>0) "))
    print("Enter array elements")
    elements = []
    for _ in range(list_size):
        elem = input()
        elements.append(elem)
    return elements

#### Unique email addresses ####

class UniqueEmailAddresses:

    def __init__(self, emails):
        self.emails = emails

    def convert(self, email):
        name, domain = email.split('@')
        if '+' in name:
            name = name[:name.index('+')]
        return "".join(["".join(name.split(".")), '@', domain])

    def numUniqueEmails(self):

        unique = set()
        for email in self.emails:
            converted_email = self.convert(email)
            unique.add(converted_email)
        return len(unique)

emails = inputStrArray()
unique_email = UniqueEmailAddresses(emails)
count_of_unique_email = unique_email.numUniqueEmails()
print(count_of_unique_email)

#### Find and replace pattern ####

class Pattern:

    def __init__(self, words, pattern):
        self.words = words
        self.pattern = pattern

    def match(self, word):
        pat = {}
        for x, y in zip(self.pattern, word):
            if pat.setdefault(x, y) != y:
                return False
        return len(set(pat.values())) == len(pat.values())

    def findAndReplacePattern(self):

        return list(filter(self.match, self.words))

words = inputStrArray()
pattern = input("Enter pattern: ")
find_and_replace = Pattern(words, pattern)
words = find_and_replace.findAndReplacePattern()
print(words)

#### Finding the user active minutes ####

class UAM:

    def __init__(self, logs, k):
        self.logs = logs
        self.k = k

    def findingUsersActiveMinutes(self):
        result = [0] * self.k
        d = {}
        for i, j in self.logs:
            if i not in d:
                d[i] = [j]
            elif j not in d[i]:
                d[i].append(j)
        for k, v in d.items():
            result[len(v) - 1] += 1
        return result

logs = inputMatrix()
k = int(input("Enter number of k: "))
uam = UAM(logs, k)
users_uam = uam.findingUsersActiveMinutes()
print(users_uam)

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