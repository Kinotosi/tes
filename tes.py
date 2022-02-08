result = []
iterasi = 50
for i in range(1, iterasi+1):
    if i % 5 == 0 and i % 3 == 0:
        result.append("Frontend Backend")
    elif i % 5 == 0:
        result.append("Backend")
    elif i % 3 == 0:
        result.append("Frontend")
    else:
        result.append(i)
print(", ".join(str(x) for x in result))