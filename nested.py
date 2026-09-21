multiple = []
for outer in range(1, 5):
    multiple.append([])
    for inner in range(1, 6):
        multiple.append(inner * outer)
print(multiple)
