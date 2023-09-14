A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

result = {}
for i in range(len(B)):
    if B[i] not in result:
        result[B[i]] = A[i]
    else:
        result[B[i]] += A[i]

print(result)