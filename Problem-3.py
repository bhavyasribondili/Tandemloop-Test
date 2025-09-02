x = int(input("Enter a number: "))
result = []
count = 0
i = 1
while count < x:
    if i % 2 != 0:
        result.append(i)
        count += 1
    i += 1

# But as per pattern in example:
# if input is even, series length is input-1
if x % 2 == 0:
    result.pop()

print(", ".join(map(str, result)))
