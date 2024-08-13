data = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = alpha.index(data[0])
y = int(data[1])-1

d = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count = 0

for dd in d:
    nx = x + dd[0]
    ny = y + dd[1]
    if nx >= 0 and ny >= 0 and nx < 8 and ny < 8:
        count+=1

print(count)