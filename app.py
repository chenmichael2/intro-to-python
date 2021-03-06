# this is a comment
# TODO built this function

def add(num, num2):
    '''
    this is suppose to add 2 numbers
    '''


name = "Johnny"

nothing = None

is_working = True
car_off = False

if nothing:
    print('This is true') 
    num = 7 
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')
else:
    print('This is not true...')

# this is another conditional
if is_working:
    print('This is working also')

# conditional -> this first item that represents 
# True, it runs that indented [block]

print(15 / 6)
print(15 // 6)

print("ace of spades".split(" "))
# => ["ace", "of", "spades"]

print("ace-of-spades".split("-"))
# => ["ace", "of", "spades"]

print("ace.of.spades".split("."))
# => ["ace", "of", "spades"]

my_scare = "boo"
my_scare.upper()

print("eggs" in "green eggs and ham")

food = "eggs"
print(food in "green eggs and ham")
print(len(food)) # => 4

statement = "my code rules"[3:9]
print(statement)

if 7 == 7:
    print('This is 7')
else:
    print('This is the second condition')

if 7 != 6:
    print('We are not the same')
else:
    print('This is the second condition')

if not 7:
    print('This is 7')
else:
    print('This is the second condition')


arr = [1, "two", 3, "four", True, False, "hello"]
print(arr[1])
print(arr[-1])

one_through_ten = list(range(10))
print(one_through_ten)

three_through_ten = list(range(3, 10))
print(one_through_ten)


a = [1, 23, 12, 99, 82]
a.sort()
print(a)

a.append(88)
print('After adding 88', a)

a.insert(1, 77)
print('After inserting 77 at index 1 ...', a)

a.pop()
print('popping....', a)

if 33 in a:
    print('This Michael Jordan number!')
else:
    print('Not in there...')

print('Is 7 a digit???', '7'.isdigit())

cat = {
  "name": 'Hamlet',
  "breed": 'American Shorthair',
  "fav_food": 'Prosciutto'
}

cat["name"] = "Garfield"
# 'Hamlet'

print('Do not feed to cat...' ,cat["fav_food"])
# 'Prosciutto'

print('this is my cat breed', cat.get("breed"))
print(cat.get("name"))
cat["age"] = 3
print(cat.get('age'))
# help(dict)

print('ITEMS', cat.items())
print('KEYS', cat.keys())

cat_keys = list(cat.keys())
print(cat_keys)


# String Interpolation
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

# 2
location = "California"
number = 6
my_second_message = f"{location} is the {number}th largest economy in the world."
print(my_second_message)

# 3
topic = 'Inflation'
num = 7
y = 1982
my_third_message = "{} is at {} percent. Highest since {}".format(topic, num, y)
print(my_third_message)

# Loops

# n = 0
# while n < 1000:
#   n += 1
#   if n % 2 == 0:
#       print(f'{n} is even...')

n = True # setting a boolean
num = 1 # setting a number that will incremented
while n: # if n get to False -> the loop stops
    if num % 2 == 0: # check to see if number is even
        print(f'{num} is even...')

        if num == 750: # check to see if num is 750
            n = False # set the boolean to False
            print('End program')
    num += 1 # adding one to num

# for loop
for i in range(1, 751): 
    if i % 2 == 0:
        print(f"{i} is even...", '**')

        if i == 750:
            print('End program')

nums = [1,2,3,55,66,44,33,22,11,33,750, 44, 66, 33,33,22]
for i in range(len(nums)):
    element = nums[i]
    if element % 2 == 0:
        print(f"{element} is even...", 'NUMS')

        if element == 750:
            print('Hi I am 750')

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]

for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == 'Los Angeles':
        print(f'{student.get("name")} wins an iPad for {student.get("city")}', 1)
        print(f"{student.get('name')} wins an iPad for {student.get('city')}", 2)

for i in range(len(students)):
    student = students[i]
    print(student.get("city"))

# Iterating through list of students
for student in students:
    print(student)

# Iterating through dict
for key in students[0]: # key to key
    print(key) # string of the key
    print('value', students[0].get(key))

# Iterating through dict PART 2
for key in students[1]: # key to key
    print(key, 'PART 2') # string of the key
    print('value', students[1][key])

# Iterating through dict PART 3
for anything in students[2]: # key to key
    print(anything, 'PART 3') # string of the key
    print('value', students[2][anything])

# Iterating through dict PART 4
for key, value in students[0].items(): # key to key
    print(key, '->', value)

def say_hello(friend="Tim"): # if we don't put a parameter, it will default to Tim
  print("Hello, {}!".format(friend))

say_hello("Tom")

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")
move("John", state="New York", city="New York")
move("Michael", state="Oregon", city="Portland")
move("Michael", "San Mateo", "California")

def music(name, genere1, genere2):
    msg = "{} loves {} and {} music"
    msg = msg.format(name, genere1, genere2)
    print(msg)

music("Michael", "Indie", "Pop")

def get_cities(students):
    '''Return a [list] of all cities from the students list'''
    # TODO Make a empty list
    # TODO Iterate through the list of student
    # TODO Apend each city in the dict to the empty list
    # TODO return the list
    result = []
    for s in students:
        # print(s)
        if s.get("city"):
            # print(s.get('city'))
            result.append(s.get('city'))
    return result

print('student cities list', get_cities(students))

def get_names(students):
    names = []
    for n in students:
        print(n)
        if n.get('name'):
            print(n.get('name'))
            names.append(n.get('name'))
    return names

print('name list: ', get_names(students))

def parse_by_city(students):
    # TODO Make a empty dict
    # TODO Iterate through the list of students and perform logic
        # if the city is not in dict
            # add the city and set that to a empty list
        # logic => if the city is in the dict
            # append student name to list
    # TODO return the dict

    result = {}
    for student in students:
        print('inside', student)
        if student.get('city'):
            if not result.get(student.get('city')):
                print('this does not exist')
                result[student.get('city')] = []
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))
            else:
                print('-----------------this exists')
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))

        print('------------------')
    return result


print('outside', parse_by_city(students))
