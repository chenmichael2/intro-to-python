from pickle import FALSE, TRUE


numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers)
print(result)
print('list', list(result))

result2 = map(lambda x: x + x, numbers)
print('result 2', list(result2))

result3 = map(lambda y: y * y, numbers)
print('result 3', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [2, 2, 2]
  
result4 = map(lambda x, y, z: x + y ** z, numbers1, numbers2, numbers3)
print('result 4',list(result4))

def triple_number(num):
    return num * 3

triple_result = map(triple_number, numbers)
print('TRIPLE', list(triple_result))

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]

ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = filter(lambda person_age: person_age < 21, ages)
print('less than 21', list(young_folks))

grown_folks = filter(lambda person_age: person_age >= 21, ages)
print('greater than 21', list(grown_folks))

def is_not_21(person_age):
    if person_age < 21:
        return True
    else:
        return False
    
def is_21(person_age):
    if person_age > 21:
        return True
    else:
        return False

young_person = list(filter(is_not_21, ages))
print('Young Person', young_person)

grown_person = list(filter(is_21, ages))
print('Grown Person', grown_person)




