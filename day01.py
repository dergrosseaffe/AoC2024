from collections import defaultdict

left, right, right_counts = [], [], defaultdict(int)
while True:
    try: a, b = input().split()
    except EOFError: break
    left.append(int(a))
    right.append(int(b))
    right_counts[int(b)] += 1

left.sort()
right.sort()

distance = 0
score = 0
for x, y in zip(left, right):
    distance += abs(x - y)
    score += x * right_counts[x]

print(distance)
print(score)