n = list(map(int, input().split()))
n1 = n[::-1]
n2 = [n[i] + n1[i] for i in range(len(n)) if i % 2 == 0]
print(*n2)

