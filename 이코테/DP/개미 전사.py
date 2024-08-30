import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
dp = [data[0],max(data[0], data[1])]

for i in range(2,n):
    dp.append(max(dp[i-2]+data[i],dp[i-1]))

print(dp[n-1])