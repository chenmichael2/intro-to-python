### TASK 1

# 1
from tabnanny import check


idx = 'abcde'.index('d')
idx += 11
print(idx) #14
idx *= 2
print(idx) # 28

#2
num = 33
isEven = num % 2 == 0
print(isEven) # false
print(not isEven) # true

#3

str1 = 'marker'
num = len('whiteboard')- len(str1)
print(num) # 4
str2 = 'bootcamp'
print(str2[num].upper()) #C
char = str2[num].lower()
print(char + '!') # c!

#4
sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence) - 1]
print(lastChar) # p
print(sentence.index(lastChar)) # 18

### TASK 3: Conditionals

#5
age = 30
if (age > 30):
    print('older than 30')
else: 
    print('younger than 30')

#6
str = 'ineapple pizza'
if (len(str) > 10):
    print('long string')
else: 
    print('short string')

if (str[0] == 'p'):
    print('starts with p')

#7
num = 15
if (num % 3 == 0):
    print('divisible by 3')
elif (num % 5 == 0):
    print('divisible by 5')

#8
num = 15
if (num % 3 == 0):
    print('divisible by 3')
if (num % 5 == 0):
    print('divisible by 5')

#9
str = 'General Assembly'
if (str[0] == str[0].upper()):
    print('starts with capital!')
if (str[len(str) - 1] == str[len(str) - 1].upper()):
    print('ends with a capital!')

#10
num = -44
if (num > 0):
    print('positive')
elif (num < 0):
    print('negative')
else: 
    print(0)

if (num % 2 == 0):
    print('even')
else: 
    print('odd')

### TASK 4
num = 11
if (num > 5): 
    print('if')
elif (num < 5):
    print('elif')
else: 
    print(5)

### TASK 5
def say_hello(name):
    msg = f'Hello {name}. How are you?'
    return msg

print(say_hello('bootcamp prep'))

def check_number(num):
    if (num > 0):
        return 'positive'
    elif (num < 0):
        return 'negative'
    else: 
        return 'zero'

print(check_number(-3))

def fizz_buzz1(max):
    for i in range(max):
        if (i % 3 == 0 and i % 5 != 0):
            print(i)
        elif (i % 5 == 0 and i % 3 != 0):
            print(i)
    return

print(fizz_buzz1(16))

def even_caps(sentence):
    newSentence = ""
    for i in range(len(sentence)):
        char = sentence[i]
        if (i % 2 == 0):
            capitalChar = char.upper()
            newSentence += capitalChar
        else: 
            newSentence += char

    return newSentence

print(even_caps('this is a new sentence'))