matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list(zip(*matrix)))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))


print(list(zip(*matrix[::-1])))