n = 1000
numbers = range(2, n, 1)

print numbers
print len(numbers)
print len(numbers) - 1
print numbers[len(numbers) - 1]
print

results = []

print len(results)

while len(numbers) > 0:
    add = numbers[0]
    results.append(add)
    
    i = len(numbers) - 1
    while i >= 0:
        if numbers[i] % add == 0:
            numbers.pop(i)
        i -= 1
        
        
print results
print len(results)
    
    
    
