arr = [1,2,3]

def tripler(arr):
    result = []

    for num in arr:
        result.append(num * 3)
    return result

print('tripler', tripler(arr))