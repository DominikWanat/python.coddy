
lst = [80,4,99,36,34]
res = []
for index, ls in enumerate (lst):
    if lst[index] < 50 or lst[index] %5 == 0:
        res.append(index)

print(res)
## Resuelto igual que en el curso