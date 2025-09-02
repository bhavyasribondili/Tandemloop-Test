x = int(input("Enter a number: "))
result = []
for i in range(x):
    result.append(2*i + 1)
print(", ".join(map(str, result)))
