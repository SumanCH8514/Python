# print how many numbers are divisable by 225 within the range of 1000 and 5000
c = 0
for i in range(1000, 5001):
    if i % 225 == 0:
        c += 1

print(f"Total numbers: {c}")