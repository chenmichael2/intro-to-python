def odd_range(num):
    arr = []
    for i in range(num):
        if(i % 2 != 0):
            arr.append(i)
    if (num % 2 != 0):
        arr.append(num)
    return arr

print(odd_range(15))