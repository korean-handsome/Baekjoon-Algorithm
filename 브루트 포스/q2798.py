N, M = map(int, input().split())
card = list(map(int, input().split()))

maxSum = 0
for i in range(0, N-2, 1):
    for j in range(i+1, N-1, 1):
        for k in range(j+1, N, 1):
            if maxSum < card[i] + card[j] + card[k] <= M:
                maxSum = card[i] + card[j] + card[k]

print(maxSum)
