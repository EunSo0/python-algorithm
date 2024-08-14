data = sorted(list(map(str,input())))

num = 0
result = ""

for i in data:
    if i.isdigit():
        num += int(i)
    else:
        result += i

print(result+str(num))
