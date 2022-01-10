a = [65, 'love', True, 45, 'peace', False, 100]

count = 0
for item in a:
    if type(item) == int:
        count += a.count(item)

print(count) 
