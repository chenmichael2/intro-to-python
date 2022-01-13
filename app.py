# this is a comment

# def add(num, num2):
#     '''
#     this is suppose to add 2 numbers
#     '''

name = "Johnny"
# print(name)

nothing = None
# print(nothing)

is_working = True
car_off = False

if nothing: 
    print('This is true')
    num = 7
    print('car is off')
elif car_off:
    print('This is the second condition')
    print('this will run if car_off is True')
elif is_working: 
    print('This is working')
else:
    print('This is not true')

string = 'my given string'

print(string[-6])
print(string[4:6])
print(string[:3])
print(string[3:])
print(string[::-1])
print(string[::2])

if 7 != 7:
    print('true')
else: 
    print('false')

# help(list)

type = "TV Shows"
stream = "Netflix"
my_first_message = f"I love to watch {type} on {stream}"

name = "Michael"
my_second_message = "{} loves to watch {} on {}".format(name, type, stream)
print(my_second_message)
