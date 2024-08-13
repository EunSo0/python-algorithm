data = input()
result = int(data[0])

for i in range(1, len(data)):
    result = max(result+int(data[i]), result*int(data[i]))

print(result)