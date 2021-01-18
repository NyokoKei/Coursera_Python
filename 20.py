arr = [1]
i = 0
while arr[-1]:
    arr.append(int(input()))
    i += 1
print(max(arr))
