lst = [0, 1, 0, 12, 3]

result = []
zero_count = 0

for x in lst:
    if x == 0:
        zero_count += 1
    else:
        result.append(x)

for i in range(zero_count):
    result.append(0)

print(result)
