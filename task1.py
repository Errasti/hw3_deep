numbers = [1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
temp = None
result = []
for number in range(len(numbers)):
    temp = numbers.pop()
    if temp in numbers and temp not in result:
        result.append(temp)
        
print(result)