multiple = []
for outer in range(1,5):
    multiple.append([])
    for inner in range(1,6):
        print("Outer: ", outer, ", Inner: ", inner, "Outer x inner ", inner * outer)
        multiple[outer-1].append( outer * inner)
print(multiples)