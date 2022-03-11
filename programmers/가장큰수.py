def solution(numbers):
    numbers = list(map(str, numbers))
    # print([num*3 for num in numbers])
    numbers.sort(key=lambda x: x*3, reverse=True)
    # print(numbers)
    return str(int(''.join(numbers)))
